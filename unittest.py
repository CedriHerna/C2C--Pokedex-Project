import unittest
import requests

class TestPokedex(unittest.TestCase):

    def test_pokemon_path(self):
        pokemonInfo = requests.get('https://pokeapi.co/api/v2/pokemon/charmander').json()
        
        self.assertEqual(pokemonInfo['id'], 4)
        self.assertEqual(pokemonInfo['name'], 'charmander')
        self.assertEqual(pokemonInfo['types'][0]['type']['name'], 'fire')

    def test_move_path(self):
        moveInfo = requests.get('https://pokeapi.co/api/v2/move/flamethrower').json()

        self.assertEqual(moveInfo['power'], 90)
        self.assertEqual(moveInfo['accuracy'], 100)

    def test_ability_path(self):
        abilityInfo = requests.get('https://pokeapi.co/api/v2/ability/blaze').json()

        englishEffect = None
        for entry in abilityInfo['effect_entries']:
            if entry['language']['name'] == 'en':
                englishEffect = entry['effect']
                break
        
        self.assertIsNotNone(englishEffect)

if __name__ == '__main__':
    unittest.main()