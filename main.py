import os
import sys
import tkinter
from http.server import SimpleHTTPRequestHandler, HTTPServer
import shutil
import time

BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
WHITE = "\033[37m"
END = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"
RESET = "\033[0m"

while True:
    cmd = input(BLUE+"$ ")
    if cmd == "shutdown":
        exit()
    elif cmd == "reboot":
        os.system("python3 start.py")
    elif cmd == "term":
        term = input("> ")
        os.system(term)
        input()
    elif cmd == "about":
        print(BLUE+"PythonOS 1.4")
        input()
    elif cmd == "md":
        
        mdp = input("Enter Directory Name to create: ")
        os.makedirs(mdp)
    elif cmd == "rd":
        try:
            rdp = input("Ender Directory Name to delete: ")
            os.removedirs(rdp)
        except FileNotFoundError:
            print(RED+"Folder not found!")
        except OSError:
            print(RED+rdp+" is not empty!")
    elif cmd == "mf":
        mfp = input("Enter File Name to create: ")
        with open(mfp, 'w') as f:
            f.write("")
    elif cmd == "rf":
        try:
            rfp = input("Enter File Name to delete: ")
            os.remove(rfp)
        except FileNotFoundError:
            print(RED+"File not found!")

    elif cmd == "rnf":
        try:
            rnfp = input("Enter File Name that you wanna rename: ")
            rnfpn = input("Enter the new File Name: ")
            os.rename(rnfp, rnfpn)
        except FileNotFoundError:
            print(RED+"File not found!")
    elif cmd == "dir":
        print(YELLOW+"Current Directory: ", os.getcwd())
    elif cmd == "cd":
        cdn = input("Enter Directory Name: ")
        os.chdir(cdn)
    elif cmd == "ls":
        os.listdir()
    elif cmd == "clear":
        os.system('cls')
    elif cmd == "edit":
        try: 
            filename = input("Enter File Name to edit: ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            with open(filename, 'a') as f:
                content = input("")
            f.write(content + "\n")
            print(f"Added Text to {filename}")
        except FileNotFoundError:
            print(f"{filename} not found.")
    elif cmd == "server":
        print("PyServer 1.0")
    elif cmd == "progripy":
        print("Progripy 1.0.0")
        print("The Package Manager for PyOS")
    elif cmd == "progripy install":
        pis = input("Enter Package Name: ")
        os.chdir("packages")
        os.chdir(pis)
        os.system("python3 install.py")
    elif cmd == "sudo":
        sudop == input("Enter PIN: ")
        if sudop == "123":
            print("ACCESS GRANTED")
        else:
            print("ACCESS DENIED")
    elif cmd == "copy":
        copy1 = input("Enter File to Copy: ")
        copy2 = input("Enter Destination to Copy: ")
        shutil.copy(copy1, copy2)
    elif cmd == "progrify":
        print("Progrify 1.0")
        print('Enter "progrify install" to install')
    elif cmd == "progrify install":
        print("Package Manager coming soon")
    elif cmd == "progrify install py-desktop":
        print("Installing...")
        time.sleep(5)
        input("Done1")
        os.system("python3 desktop.py")