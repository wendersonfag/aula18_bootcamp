import requests
from database.db import SessionLocal, engine, Base
from model.m_pokemon import Pokemon
from views.v_pokemon import PokemonSchame

Base.metadata.create_all(bind=engine)

def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    print(response)
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchame(name=data['name'], type=types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchame) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon