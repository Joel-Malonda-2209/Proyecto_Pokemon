import requests
import json

def get_first_generation_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print("Error al obtener los datos de los Pokémon de la primera generación")
        return []

def get_pokemon_info(pokemon_url):
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        data = response.json()
        pokemon_data = {
            'name': data['name'].capitalize(),
            'abilities': [ability['ability']['name'].capitalize() for ability in data['abilities']],
            'type': data['types'][0]['type']['name'].capitalize(),
            'stats': {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in data['stats']},
            'moves': [move['move']['name'].capitalize() for move in data['moves']]
        }
        return pokemon_data
    else:
        print(f"Error al obtener la información del Pokémon: {pokemon_url}")
        return {}

def main():
    pokemon_first_generation = get_first_generation_pokemon()
    pokemon_data = []
    for pokemon in pokemon_first_generation:
        pokemon_info = get_pokemon_info(pokemon['url'])
        if pokemon_info:
            pokemon_data.append(pokemon_info)
    
    with open('pokemon_first_generation.json', 'w') as file:
        json.dump(pokemon_data, file, indent=4)

if __name__ == "__main__":
    main()
