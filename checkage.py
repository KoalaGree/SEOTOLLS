import requests
import os
import time
import threading


os.system('cls' if os.name == 'nt' else 'clear')


datadomain = input(" List Domain.txt ? ")
check_file = os.path.isfile("Result_Check_AGE.txt")
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Result_Check_AGE.txt")
    elif ('n') or ('N') in ask1:
        pass

if check_file == 0:
    new = open("Result_Check_AGE.txt", "x")


def CheckAge():
    with open(datadomain, 'r') as listage:
        countdata = len(open(datadomain).readlines())
        linedata = listage.read().splitlines()
        for lines in linedata:
            countdata -= 1

            url = "https://www.iplocation.net/domain-age"

            payload='domain=boipokaderaddakhana.com&submit=Submit'
            headers = {
            'authority': 'www.iplocation.net',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'origin': 'https://www.iplocation.net',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.iplocation.net/domain-age',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'visid_incap_877543=8s2OUYy2Sg6cyRsCTLLn5XgW0mAAAAAAQUIPAAAAAAAXTHtUIldcupqOI/NinOWQ; incap_ses_1118_877543=tleLAeSR4x7Fv1Vqbu+DD3kW0mAAAAAAYTw2t8WEjf5DuTIJtcs1Wg==; __utmzz=utmcsr=google|utmcmd=organic|utmccn=(not set)|utmctr=(not provided); __utmzzses=1; _ga=GA1.2.602922067.1624381077; _gid=GA1.2.240534762.1624381077; PHPSESSID=d6e02dc0f13bc193f62f0570c7e59c95; _pbjs_userid_consent_data=3524755945110770; cto_bidid=7svLT19pbzdjNW5LaWRIWHFYZnN6dnZBJTJCdHZwNUp6MVMyTUZSNnRDcWZ5UTR0cWJOSWdIMEJJRWhPZlNxSW9hYUE3dWNqeGRpMkdoUmE2NjNHeGY5ME9MVXBZZUJxUThPc3Z1WDZUTDVqWjJBekwlMkJDcTQ1UG1uVGdGdG9VVU14Yk1EeEE; cto_bundle=eIW6b19HNTJCRHp1VlZZbEtmNUdMJTJGT1ByY2xxamRoR0pvczdvTHE0RlglMkJPY2V6UFQlMkJJalpzbWw5WDlMbzRWUWRpOEhieFN0MlNVZU4lMkJRQmhQYnVLT1VoOU1EMTlMcHVEeWJ1a2ZBQlI2UFZwd3BNakYlMkIwbFRsTFg5Ym9rNzdNNjRQcTBWc0FhOE4ybWJtMTloT3ZjM20yeHNRJTNEJTNE; __gads=ID=cddd957c481769e7:T=1624382007:S=ALNI_MYc0Z2GvHsk9Tqa2tbvNvyy1aaigQ; incap_ses_1118_877543=ipeaYrdgqCqF9FVqbu+DD+ka0mAAAAAAHWQWzvlI8cBee5DzMayS0Q==; visid_incap_877543=ArDO8ZlfR5e5PP9oTnVMMKMa0mAAAAAAQUIPAAAAAACyUWII3FF3lYxmAHykrT2H; PHPSESSID=c698f669a0ad32090a66e04eee196dcf'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if  "Domain Age " > str('3 years') in response.text:
                tmp = open("tmp_result.txt", "+a")
                tmp.write(lines)
                tmp.close()
                print("[ PERFECT ] More Than 3 Years or 5 Years - "+lines)
                j = open("Result_Check_AGE.txt", "+a")
                j.write(lines)
                j.write('\n')
                j.close()
                os.remove("temp_result.txt")
                # print("Good Job")
            else:
                print(" [ To Young ] Under 2 Years - "+lines)
threading.Thread(target=CheckAge).start()