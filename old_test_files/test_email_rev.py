import os
import sys
import time

path = os.path.abspath(sys.argv[0])

print(path)

os.system("REG Add /?")
time.sleep(10)