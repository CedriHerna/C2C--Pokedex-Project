import requests
import webbrowser

# Something I might use later so that I can find pokemon images.
# data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()
# sprite_url = data['sprites']['front_default']

# webbrowser.open(sprite_url)

print("**********Pokemon Pokedex!**********")
try:
    retrieved_pokemon = input("What pokemon would you like to look up?").lower()
    retrieved_pokemon_data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{retrieved_pokemon}').json()
    for move in retrieved_pokemon_data['moves']:
        print(move['move']['name'])

except: 
    retrieved_pokemon = input("Please try again!")

