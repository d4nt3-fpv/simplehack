from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# Press and release space
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)
time.sleep(0.01)
keyboard.type("cmd")
time.sleep(0.05)
keyboard.press(Key.enter)
time.sleep(0.05)
keyboard.release(Key.enter)
###

time.sleep(0.05)
keyboard.type("color")

