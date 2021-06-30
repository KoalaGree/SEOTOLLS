import requests
import threading
import os
import os.path
os.system('cls' if os.name == 'nt' else 'clear')

listscan = input(" Url List ? ")
endpoints = input(" Endpoint List ? ")
check_file = os.path.isfile("Shell_Found.txt")
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Shell_Found.txt")
    elif ('n') or ('N') in ask1:
        pass

if check_file == 0:
    new = open("Shell_Found.txt", "x")

def Shellfind():
    try:
        with open(listscan, 'r') as urllist :
            counts = len(open(listscan).readlines())
            lineurl = urllist.read().splitlines()
            for lines in lineurl:
                with open(endpoints, 'r') as k:
                    cot = len(open(endpoints).readlines())
                    linek = k.read().splitlines()
                    for key in linek:
                        joins = lines + "/" + key
                        res = requests.get(joins)
                        if '<php' in res.text:
                            tmp = open("temp_results.txt", "+a")
                            tmp.write(joins)
                            tmp.close()
                            print("[ ShellFinder ] Possible shell found at - "+joins)
                            oprs = open("Shell_Found.txt", "+a")
                            oprs.write(joins)
                            oprs.write("\n")
                            oprs.close()
                            os.remove("temp_results.txt")
                        else:
                            print("[ ShellFinder ] Shell Not Found - "+joins)
    except Exception as e:
        print(e.args)
threading.Thread(target=Shellfind).start()
