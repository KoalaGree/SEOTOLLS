import requests
import threading
import os
import os.path
os.system('cls' if os.name == 'nt' else 'clear')

listscan = input(" Url List ? ")
check_file = os.path.isfile('Founded.txt')
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Founded.txt")
    elif ('t') or ('T') in ask1:
        pass

if check_file == 0:
    open('Founded.txt', 'x')

def Wordpress():
    try:
        with open(listscan, 'r') as url:
            counts = len(open(listscan).readlines())
            line = url.read().splitlines()
            for lines in line :
                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Cache-Control': 'max-age=0',
                }

                response = requests.get('http://kampunginggriscamp.id/wp-admin/install.php', headers=headers).text
                # print(response.text)
                if 'Continuar' in response:
                    tmp = open("temp_result.txt", '+a')
                    tmp.write(lines)
                    tmp.close()
                    print('[ WordPress ] Founded WordPress - ' +lines)
                    oprs = open("Founded.txt", '+a')
                    oprs.write(lines)
                    oprs.write('\n')
                    oprs.close()
                    os.remove("temp_result.txt")
                elif 'Already Installed' in response:
                    print('[ WordPress ] Already Installed')

    except Exception as e:
        print(e.args)
threading.Thread(target=Wordpress).start()