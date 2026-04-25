import requests
import webbrowser

# Functions:
def getDecision():
    while True:
        decision = input("What do you want to look up? Choose either to look up a pokemon, move, or ability from the list." \
        "\n1. Pokemon" \
        "\n2. Move" \
        "\n3. Ability" \
        "\n").lower() 

        goodDecision = ["1.", '1', 'pokemon', "2.", "2", "move", "3.", '3', "ability"]
        
        if decision in goodDecision:
            if decision == "1." or decision == "1" or decision == "pokemon":
                return "1"
            elif decision == "2." or decision == "2" or decision == "move":
                return "2"
            elif decision == "3." or decision == "3" or decision == "ability":
                return "3"
            else:
                print("Error")
        else:
            print("Please try again. Either type in the number or the name of the option. Examples include: \"pokemon\" or \"1\"")

def pokemonPath():
    # What pokemon are you looking for?
    # Format:
    # Pokemon Number| Pokemon Name | Pokemon Type 
    pokemon = input("What pokemon are you looking for? ")
    while True:
        try:
            pokemonInfo = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
            break
        except:
            pokemon = input("Watch out for the spelling! Please try to input the pokemon's name again. ")
    
    pokemonNumber = pokemonInfo['id']

    pokemonType = ""
    for type in pokemonInfo['types']:
        pokemonType += type['type']['name'] + "/"
    pokemonType = pokemonType[:-1]

    sprite_url = pokemonInfo['sprites']['front_default']
    print(f"#{pokemonNumber} | {pokemon.capitalize()} | {pokemonType.capitalize()} Type")
    webbrowser.open(sprite_url)

def movePath():
    # We want to ask the user what move they are looking for.
    # Damage | Accuracy | Type of Move | Pokemon Type of the Move | Priority
    
    move = input("What move are you looking for? ")
    while True:
        try:
            moveInfo = requests.get(f'https://pokeapi.co/api/v2/move/{move}').json()
            break
        except:
            move = input("Watch out for the spelling! Please try to input the move's name again. ")
    
    damage = moveInfo['power']
    accuracy = moveInfo['accuracy']
    TypeMove = moveInfo['type']['name']
    PokemonTypeMove = moveInfo['damage_class']['name']
    priority = moveInfo['priority']

    print(f"{move.capitalize()} | {damage} Damage | {accuracy}% Accuracy | {TypeMove.capitalize()} | {PokemonTypeMove.capitalize()} | Priority: {priority}")

def abilityPath():
    ability = input("What ability are you looking for? ")
    while True:
        try: 
            abilityInfo = requests.get(f"https://pokeapi.co/api/v2/ability/{ability}").json()
            break
        except:
            ability = input("Watch out for the spelling! Please try to input the ability's name again. ")
    
    for entry in abilityInfo['effect_entries']:
        if entry['language']['name'] == 'en':
            ability = entry['effect']
            break
    
    print("This is this the effect of the ability:" \
    f"\n{ability}")


# Key Path


print("**********Pokemon Pokedex!**********")
# The user chooses their path. Either looking for a pokemon, move, or ability.
choice = getDecision()
while True:
    if choice == "1":
        pokemonPath()
    elif choice == "2":
        movePath()
    elif choice == "3":
        abilityPath()
    else:
        break

    yesNo = input("Is there anything else you want to look up? (yes/no): ").lower()
    while yesNo not in ["yes", "no"]:
        yesNo = input("Please enter yes or no!").lower()
    if yesNo == "yes":
        choice = getDecision()
    else:
        break

print("Bye Bye!")
