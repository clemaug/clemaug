import streamlit as st
import requests

# Getting the Pokemon informations using the API PokeAPI
def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'].capitalize(),
            'type': ', '.join([t['type']['name'].capitalize() for t in data['types']]),
            'weight': data['weight'] / 10,  
            'height': data['height'] / 10,
            'image_url': data['sprites']['front_default'],
        }
    else:
        return None

# Getting the Pokemon description using the API PokeAPI
def get_pokemon_description(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = [entry['flavor_text'] for entry in data['flavor_text_entries'] if entry['language']['name'] == 'en'][0]
        return description
    else:
        return None

# Streamlit interface
st.title("Pokedex")
pokemon_name = st.text_input("Nom du Pokemon")
if st.button("Rechercher"):
    if pokemon_name:
        pokemon_info = get_pokemon_info(pokemon_name)
        pokemon_description = get_pokemon_description(pokemon_name)
        if pokemon_info and pokemon_description:
            st.subheader(f"Nom: {pokemon_info['name']}")
            st.write(f"Type: {pokemon_info['type']}")
            st.write(f"Poids: {pokemon_info['weight']} kg")
            st.write(f"Taille: {pokemon_info['height']} m")
            st.image(pokemon_info['image_url'], caption=pokemon_info['name'], use_column_width=True)
            st.write("Description:")
            st.write(pokemon_description)
        else:
            st.warning("Pokemon not found")

# This is a streamlit APP
