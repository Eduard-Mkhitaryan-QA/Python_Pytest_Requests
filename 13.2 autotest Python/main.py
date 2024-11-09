import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c99ae31dfd1fd96403f22eda9299c4b3'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}



body_registration = {
    "trainer_token": TOKEN,
    "email": "Ed@yandex.ru",
    "password": "Q3spmwjm"
}

body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

body_new_name = {
    "pokemon_id": "127524",
    "name": "generate",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "127530"
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (response.text)'''

'''Создание покемона'''
response_create_pokemon=requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print (response_create_pokemon.text)

pokemon_id = response_create_pokemon.json()['id']
print (pokemon_id)

'''Изменение имени покемона'''
response_new_name=requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print (response_new_name.text)


'''Поймать в покебол'''
response_add_pokeball=requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print (response_add_pokeball.text)











