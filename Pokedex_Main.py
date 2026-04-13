import requests
data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu').json()
print(data['name'], data['types'])