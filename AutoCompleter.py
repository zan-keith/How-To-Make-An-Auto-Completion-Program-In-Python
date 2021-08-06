#cd C:\Users\Hydrogen\Desktop\P.Y.T.H\Auto comp project
import keyboard
import numpy as np
import pandas as pd
from win10toast import ToastNotifier
import os

path = os.getcwd()
print(path)
path=path+'\\Key_abbr.csv'
print(path)
toaster = ToastNotifier()
toaster.show_toast("Autocompletion Extention",
                   "The Program has started press combination [esc+shift+q] to close",
                   icon_path="wolf.ico",
                   duration=5)

import subprocess as sp
sp.Popen(['notepad.exe', path])
try:
    data = pd.read_csv('Key_abbr.csv')
except:
    print('unable to find the required files')
abr=data['Press']
result=data['Result']

x=np.array(abr)
y=np.array(result)

keyboard.add_hotkey('shift+"', lambda: (keyboard.write('"') ,keyboard.release('shift'),keyboard.press_and_release('left arrow')))
keyboard.add_hotkey("'", lambda: (keyboard.write("'") ,keyboard.release('shift'),keyboard.press_and_release('left arrow')))
keyboard.add_hotkey('shift+{', lambda: (keyboard.write('}') ,keyboard.release('shift'),keyboard.press_and_release('left arrow')))
keyboard.add_hotkey('[', lambda: (keyboard.write(']') ,keyboard.release('shift'),keyboard.press_and_release('left arrow')))
keyboard.add_hotkey('shift+(', lambda: (keyboard.write(')') ,keyboard.release('shift'),keyboard.press_and_release('left arrow')))

keyboard.add_abbreviation(x[0], y[0])
keyboard.add_abbreviation(x[1], y[1])
keyboard.add_abbreviation(x[2], y[2])
keyboard.add_abbreviation(x[3], y[3])
keyboard.add_abbreviation(x[4], y[4])
keyboard.add_abbreviation(x[5], y[5])
keyboard.add_abbreviation(x[6], y[6])
keyboard.add_abbreviation(x[7], y[7])
keyboard.add_abbreviation(x[8], y[8])
keyboard.add_abbreviation(x[9], y[9])




keyboard.wait('esc+shift+q')
