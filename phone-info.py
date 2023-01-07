import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
from pystyle import *
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
white = Col.white
green = Col.light_green
purple = Col.light_blue
red = Col.light_red
copy = "╔═════════════════════════════════╗\n║ Copyright by mfr                ║\n║ https://github.com/mfr-fr       ║\n╚═════════════════════════════════╝"
banner = "\n██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗\n██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝\n██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  \n██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  \n██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗\n╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝\n                                           \n██╗███╗   ██╗███████╗ ██████╗              \n██║████╗  ██║██╔════╝██╔═══██╗             \n██║██╔██╗ ██║█████╗  ██║   ██║             \n██║██║╚██╗██║██╔══╝  ██║   ██║             \n██║██║ ╚████║██║     ╚██████╔╝             \n╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝\n╔═════════════════════════════════╗\n║ Copyright by mfr                ║\n║ https://github.com/mfr-fr       ║\n╚═════════════════════════════════╝"

#def phone
def phone():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.green_to_red, banner, 2))
    print(f"{red}ONLY FOR FRENCH NUMBERS {purple}\nExample : {white}+33757137389{purple}\nLeave : {white}99")
    phone = input(f"{purple}Phone number :{white} ")
    if phone == '99':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(quit())
    if phone == '':
        boucle()
    else :
        os.system('cls' if os.name == 'nt' else 'clear')
        number = phonenumbers.parse(phone)
        valid = phonenumbers.is_valid_number(number)
        country = geocoder.description_for_number(number,'fr')
        opera = carrier.name_for_number(number,'fr')
        timeZone = timezone.time_zones_for_number(number)
        possible= phonenumbers.is_possible_number(number)
        valid = phonenumbers.is_valid_number(number)
        if valid == True and opera != "":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Colorate.Vertical(Colors.green_to_red, banner, 2))
            print((f"{green}> {purple}Possible number : {white}{possible} \n{green}> {purple}Valid number : {white}{valid} \n{green}> {purple}Phone number : {white}{phone} \n{green}> {purple}Country : {white}{country} \n{green}> {purple}Operator : {white}{opera} \n{green}> {purple}TimeZone : {white}{timeZone}"))
            input("\nPress enter to close")
            os.system('cls' if os.name == 'nt' else 'clear')
            boucle()

#def boucle
def boucle():
    phone()


#Copyrights
os.system('Title  Phone-info ║ BY MFR')
os.system('cls' if os.name == 'nt' else 'clear')
print(copy)
time.sleep(2)
phone()
