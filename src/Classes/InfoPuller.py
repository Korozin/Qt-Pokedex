import sys, json, requests

class PokemonInfo:
    def __init__(self, pokemon_id):
        self.pokemon_id = pokemon_id.lower()
        self.pokemon_data = None
        self.species_data = None
        self.evolution_chain = None

    def fetch_pokemon_data(self):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_id}/")
        self.pokemon_data = response.json()

    def fetch_species_data(self):
        response = requests.get(self.pokemon_data['species']['url'])
        self.species_data = response.json()

    def get_id(self):
        return self.pokemon_data['id']

    def get_name(self):
        return self.pokemon_data['name'].capitalize()

    def get_abilities(self):
        abilities = []
        for ability in self.pokemon_data['abilities']:
            abilities.append(ability['ability']['name'].capitalize())
        return abilities

    def get_moves(self):
        moves = []
        for move in self.pokemon_data['moves']:
            for version in move['version_group_details']:
                if (version['level_learned_at'] == 1):
                    moves.append(move['move']['name'].capitalize())
                    break
        return moves

    def get_stats(self):
        stats = {}
        for stat in self.pokemon_data['stats']:
            stats[stat['stat']['name'].upper()] = stat['base_stat']
        return stats

    def get_types(self):
        types = []
        for pokemon_type in self.pokemon_data['types']:
            types.append(pokemon_type['type']['name'].capitalize())
        return types

    def fetch_evolution_chain(self):
        response = requests.get(self.species_data['evolution_chain']['url'])
        evolution_data = response.json()
        evolution_chain = []
    
        # Traverse the entire evolution chain and add all the names to the list
        current_evolution = evolution_data['chain']
        while True:
            evolution_chain.append(current_evolution['species']['name'].capitalize())
            if current_evolution['evolves_to']:
                current_evolution = current_evolution['evolves_to'][0]
            else:
                break
    
        self.evolution_chain = evolution_chain

    def get_evolution_chain(self):
        if self.evolution_chain is None:
            self.fetch_species_data()
            self.fetch_evolution_chain()
        return self.evolution_chain

    def get_sprite_url(self):
        return self.pokemon_data['sprites']['front_default']

    def get_info(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'types': self.get_types(),
            'abilities': self.get_abilities(),
            'moves': self.get_moves(),
            'evolution_chain': self.get_evolution_chain(),
            'stats': self.get_stats(),
            'sprite_url': self.get_sprite_url()
        }


'''
# Initialize either using Pkmn name or ID.
pokemon = PokemonInfo("1")

# Fetch the Pokemon data and species data
pokemon.fetch_pokemon_data()
pokemon.fetch_species_data()

# Get the relevant information as a dictionary
pokemon_info = pokemon.get_info()
# JSON Pretty dict if you don't want to format manually
#pokemon_info = json.dumps(pokemon.get_info(), indent=4)

# Print the relevant information
print("ID:", (pokemon_info['id']))
print("NAME:", (pokemon_info['name']))
print("TYPE:", (', '.join(pokemon_info['types'])))
print("ABILITIES:", (', '.join(pokemon_info['abilities'])))
print("MOVES:", (', '.join(pokemon_info['moves'])))
print("EVOLUTION CHAIN:", (' > '.join(pokemon_info['evolution_chain'])))
print("STATS:")
for stat, value in pokemon_info['stats'].items():
    print(f"    {stat}: {value}")
print("SPRITE URL:", pokemon_info['sprite_url'])
'''
