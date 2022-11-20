# ========================================================================
#                   ServerLookup v1.0 github.com/AdvancedBan
#                            Made by AdvancedBan
#                              @0xAdvancedBan
# ========================================================================


import requests as r
import json
import os
from colorama import Fore, init

from mcstatus import JavaServer
from config.mc_replace_text import mc_replace_text_mccolors, mc_replace_text_json

# COLORS

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

#API

mcsrvstat_api = "https://api.mcsrvstat.us/2/"

def request():
 
    os.system("cls")
    server = input("Enter server ip >> ")
    srv = JavaServer.lookup(server)
    response_srv = srv.status()
    motd = mc_replace_text_mccolors(response_srv.description)

    response = r.get(f"{mcsrvstat_api}{server}")
    r_data = response.json()

    if  response.ok:
        version = r_data['version']
        online = r_data['online']
        ip = r_data['ip']
        port = r_data['port']
        print(f"{lblack}[{lblue}On{white}line{lblack}]{white}  : {online}")
        print(f"{lblack}[{lblue}I{white}P{lblack}]{white}      : {ip}:{port}")
        print(f"{lblack}[{lblue}MO{white}TD{lblack}]{white}    : {motd}{white}")
        print(f"{lblack}[{lblue}Ver{white}sion{lblack}]{white} : {version}")
        print(f"{lblack}[{lblue}Play{white}ers{lblack}]{white} : {response_srv.players.online}/{response_srv.players.max}")
        input("Press enter to exit")
    else:
        print("An error has occurred !")
        input("Press enter to exit")
    request()

request()
