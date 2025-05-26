import requests


#Corzinha:
AZUL = '\033[94m'


resposta = requests.get('https://randomuser.me/api/?results=10&inc=name,email,nat')
users = resposta.json()

usuario = users["results"][0]

print(f"{AZUL}Nome: {usuario['name']['first']} {usuario['name']['last']}{RESET}")
print(f"{AZUL}Email: {usuario['email']}{RESET}")
print(f"{AZUL}Nacionalidade: {usuario['nat']}{RESET}")

