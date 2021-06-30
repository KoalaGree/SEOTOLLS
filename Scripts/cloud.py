import requests
import os
import os.path
import threading
os.system('cls' if os.name == 'nt' else 'clear')


listurl = input(" List Url.txt ? ")
check_file = os.path.isfile("Success_Cloud_Downloaded.txt")
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Success_Cloud_Downloaded.txt")
    elif ('n') or ('N') in ask1:
        pass

if check_file == 0:
    new = open("Success_Cloud_Downloaded.txt", "x")

def cloud():
    try:
        with open(listurl, 'r') as listu:
            counturl = len(open(listurl).readlines())
            line = listu.read().splitlines()
            for lines in line:
                url = "https://offcloud.com/api/cloud?key=h3MuNTwhzVzas9rJoUxvlRDpdZz6tFXu&url={}".format(lines)
                payload={}
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
                }

                response = requests.request("GET", url, headers=headers, data=payload)
                hasil = response.json()
                if hasil == 'true':
                    tmp = open("temp_results.txt", "+a")
                    tmp.write(lines)
                    tmp.close()
                    print("[ Offcloud - Cloud ] Downloading With This Url - "+lines)                
                    oprs = open("Success_Cloud_Downloaded.txt", "+a")
                    oprs.write(lines)
                    oprs.write("\n")
                    oprs.close()
                    os.remove("temp_results.txt")
                elif hasil == 'Incorrect address specified':
                    print("[ Offcloud - Cloud ] Error Downloading Please Check Your File!!")
                elif hasil == 'url parameter is not specified':
                    print("[ Offcloud - Cloud ] Please Check Your Parameters !!!")
    except Exception as e:
        print(e.args)
threading.Thread(target=cloud).start()