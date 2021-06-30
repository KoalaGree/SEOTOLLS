from re import findall
import requests
from bs4 import BeautifulSoup
import requests
import threading
import os
import os.path
import time
import random
os.system('cls' if os.name == 'nt' else 'clear')
print("""
 __            ___         
|  \ _ .. _ |   | _  _ | _ 
|__/(_|||(_||   |(_)(_)|_) 
       //                  
""")


listip = input("List IP File : ")
check_file = os.path.isfile("Result.txt")
if check_file == 1:
    ask1 = input(" Hapus bos ? ")
    if ('y') in ask1 or ('Y') in ask1:
        os.remove("Result.txt")
    elif ('n') in ask1 or ('N') in ask1:
        pass

if check_file == 0:
    new = open("Result.txt", "x")

# listproxy = input("List Proxy File : ")
# def proxys():
#     line = open(listproxy).read().splitlines()
#     myline = random.choice(line)
#     return myline



def ReverseTime():
    with open(listip, 'r') as iplist:
        countip = len(open(listip).readlines())
        line = iplist.read().splitlines()
        # proxy = {
        #     "http" : "http://"+proxys(),
        # }
        for lines in line:
            countip -= 1
            url = "https://osint.sh/reverseip/"

            payload="domain="+str(lines)
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://osint.sh',
            'Connection': 'keep-alive',
            'Referer': 'https://osint.sh/reverseip/',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers'
            }

            response = requests.request("POST", url, headers=headers, data=payload).text
            if "<th>Domain</th>" in response:
                soup = BeautifulSoup(response, "html.parser")
                table = soup.find("table", attrs={"class": "bmw-table css-serial"})
                for row in table.findAll("tr"):
                    #print (row)
                    cells = row.findAll("td")
                    cols = [element.text.strip() for element in cells]
                    for col in cols:
                        tmp = open("temp_result.txt","+a")
                        tmp.write(cols[2])
                        tmp.write("\n")
                        tmp.close()
                        counts = len(open("temp_result.txt").readlines())
                        print("[ AdaBosss ] Dapet Web Dari IP "+lines)
                        f = open("Result.txt","+a")
                        f.write(cols[2])
                        f.write("\n")
                        f.close()
                        os.remove("temp_result.txt")
                        
            else:
                print("Waduhh Bos Kayaknya Gak Ada List Domainnya Bos")
# print(response.text)
threading.Thread(target=ReverseTime).start()
