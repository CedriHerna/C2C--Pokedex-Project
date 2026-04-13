import requests
import webbrowser

data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()
sprite_url = data['sprites']['front_default']

webbrowser.open(sprite_url)