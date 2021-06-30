import requests
import os
import time
import threading

os.system('cls' if os.name == 'nt' else 'clear')


listdomain = input(" List Domain.txt ? ")
check_file = os.path.isfile("Result_Check_NS.txt")
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Result_Check_NS.txt")
    elif ('n') or ('N') in ask1:
        pass

if check_file == 0:
    new = open("Result_Check_NS.txt", "x")


def CheckNS():
    with open(listdomain, 'r') as listns:
        countdomain = len(open(listdomain).readlines())
        line = listns.read().splitlines()
        for lines in line:
            countdomain -= 1
            url = "https://www.infobyip.com/ipbulklookup.php"

            payload='ips={}&record_type=ns&_p1=2176'.format(lines)
            headers = {
            'authority': 'www.infobyip.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://www.infobyip.com',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.infobyip.com/ipbulklookup.php',
            'accept-language': 'en-US,en;q=0.9'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if 'NAMECHEAP-NET' in response.text:
                tmp = open("temp_results.txt", "+a")
                tmp.write(lines)
                tmp.close()
                print("[ CHECKED ] This Domain Is Namecheap.Inc - "+lines)
                oprs = open("Result_Check_NS.txt", "+a")
                oprs.write(lines)
                oprs.write("\n")
                oprs.close()
                os.remove("temp_results.txt")
            else:
                print("[ CHECKED ] This Domain Isn't Namecheap.Inc - "+lines)
            # print(response.text)

threading.Thread(target=CheckNS).start()