import os;
import tkinter as tk
from tkinter import filedialog
import json


#default settings 
#if settings dont exist -,-
defaut_settings={
   "image":[".png",".jpg"],
   "videos":[".mp4"],
   "music":[".mp3"],
   "pack":[".zip"],
   "documents":[".txt"],
}

#clear console;
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()

#loading settings if you not have settings.json else use this settings;
def check_settings():
    if os.path.exists("settings.json"):
        r = open('settings.json')
        data = json.load(r)
        r.close()
        return data
    else:
        r = open("settings.json", "w") 
        r.write(json.dumps(defaut_settings))
        r.close()
        return defaut_settings
settings = check_settings()

#checking folders to sort if no exist, CREATE!
def check_folders(a=os.getcwd()):
    for r in settings:
        if os.path.exists(r)==False:
            os.makedirs(r)
# check_folders()

#Make chatGPT... Tfu... js js js js js!!!!!
def Includes(sequence, item):
    return item in sequence

#searching searching searching!!!
# a = search string of name file .txt | b where. location!
def search_file(a,b=os.getcwd()):
    for r in os.listdir(b):
        if Includes(r,a):return r
# search_file(".txt")

#moving files maybe wrong, but working xD
def move_file(a,b):
    if os.path.isfile(a) and os.path.isdir(b):
        c = os.path.abspath(a)
        os.replace(c, os.path.join(b, os.path.basename(a)))
    else: print("brak pliku lub folderu docelowego!!!")

#a where sort/ b output sorting
def sort(a=os.getcwd(),b=os.getcwd()):
    check_folders(b)
    for r in settings:
        if len(settings[r])!=0:
            z = settings[r]
            for l in z:
                if search_file(l,a):
                    move_file(search_file(l,a), os.path.join(b, r))
#sort()

def start():
    input("""
HELLO WORLD!</br>
DO YOU WANNA SORT YOUR FUCKING DESKTOP? OR OTHERS FOLDER?
IF YES. GOOD, IN settings.json YOU HAVE MORE SETTINGS WHAT FILES YOU WANT SORTING
IF YOU ARE NOT STUPID YOU CAN DO IT
CLICK ENTER OR WHAT YOU WANT TO BE CONTINUE...
""")
start()

def tree_thing():
    input("""
NOW YOU NEED A CHOOSE LOCATION WHERE WE SORTING
CLICK ENTER AND CHOOSE YOU LOCATION!
""")
    sort_dir = filedialog.askdirectory()
    if os.path.isdir(sort_dir):
        print('LOCATION CHOSEN! your location: '+ sort_dir)
        input("""
SELECT WHERE THE SORTED FILES WILL BE SAVED 
""")
    output_dir = filedialog.askdirectory()
    if os.path.isdir(output_dir):
        print('YOUR SORTED FILES ARE LOCATED IN: '+ sort_dir)
        sort(sort_dir,output_dir)
tree_thing()
