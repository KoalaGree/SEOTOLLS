import requests
from re import findall
import threading
import os
import os.path
os.system('cls' if os.name == 'nt' else 'clear')


listdomain = input(" List Domain.txt ? ")
check_file = os.path.isfile("Result_Check_Domains.txt")
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Result_Check_Domains.txt")
    elif ('n') or ('N') in ask1:
        pass

if check_file == 0:
    new = open("Result_Check_Domains.txt", "x")

def Check_Domains():
    with open(listdomain, 'r') as listsd:
        countdomain = len(open(listdomain).readlines())
        line = listsd.read().splitlines()
        for lines in line:
            countdomain -= 1
            payload = {}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Connection': 'keep-alive'
            }

            response = requests.get('http://'+str(lines)+'/cgi-sys/defaultwebpage.cgi', headers=headers, data=payload)
            if 'SORRY!' in response.text:
                tmp = open("temp_results.txt", "+a")
                tmp.write(lines)
                tmp.close()
                print(" [ ACCESSED ] This Domains Can Add - "+lines)
                oprs = open("Result_Check_Domains.txt", "+a")
                oprs.write(lines)
                oprs.write("\n")
                oprs.close()
                os.remove("temp_results.txt")
            else:
                print("[ UNACCESSED ] This Domains - "+lines)


threading.Thread(target=Check_Domains).start()
# print("==================================")
# count_results = len(open("Result_Check_Domains.txt").readlines())
# print(" Total Results : "+str(count_results))
