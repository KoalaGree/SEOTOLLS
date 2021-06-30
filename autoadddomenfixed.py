from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException
import time
import sys
from os import system, name 
import os
import pyautogui



def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
clear()
userme = 'echotwvx' # Ganti Username dengan Username yang akan di buat login
passwd = 'Bajingan123!@#' # Ganti Password dengan Password yang akan di buat login
# pathfilehtml = 'C:/Users/andyc/OneDrive/Documents/revip/index.html' # Ganti ke path file html yang ingin di upload
print(" AL HAIL GONDRONG GANTENG ")
listdomain = input(' List Domain ? ')
totallist = len(list(open(listdomain)))
check_file = os.path.isfile("Result_Domains_Added.txt")
if check_file == 1:
    ask1 = input(" Delete Previous Result ? ")
    if ('y') or ('Y') in ask1:
        os.remove("Result_Domains_Added.txt")
    elif ('n') or ('N') in ask1:
        pass
if check_file == 0:
    new = open("Result_Domains_Added.txt", "x")
list = open(listdomain, 'r')
while True:
    domainlist = list.readline().replace('\n','')
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36")
    driver = webdriver.Chrome(r'C:/Users/Thinkpad/Documents/KONTOL/chromedriver.exe', chrome_options=opts) # Ganti path Chromedriver.exe
    driver.get('https://echoesoffear.com:2083/') # Ganti Url ke Url yang ingin di login
    time.sleep(10)
    usermeinput = driver.find_element_by_id('user')
    usermeinput.send_keys(userme)
    passwdinput = driver.find_element_by_id('pass')
    passwdinput.send_keys(passwd)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"login-form__submit btn")]'))).click()
    time.sleep(10)
    content = driver.page_source
    result = content.find('Current User')
    if (result != -1):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="icon-addon_domains"]/following-sibling::a[1]'))).click()
        content = driver.page_source
        result = content.find('Create an Addon Domain')
        if (result != -1):
            domaininputs = driver.find_element_by_xpath('//input[@class="form-control hide-clear-button"]')
            domaininputs.send_keys(domainlist)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="btn btn-primary"]'))).click()
            content = driver.page_source
            result = content.find('If you would like to manage the files for this domain')
            tmp = open("temp_results.txt", "+a")
            tmp.write(domainlist)
            tmp.close()
            print("[ SUCCESS ] Added To Cpanel This Domain - "+domainlist)
            oprs = open("Result_Domains_Added.txt", "+a")
            oprs.write(domainlist)
            oprs.write(\n)
            oprs.close()
            os.remove("temp_results.txt")
            # if (result != -1):
            #     # tmp = open("temp_result.txt", "+a")
            #     # tmp.write(domainlist)
            #     # tmp.close()
            #     # countz = len(open("temp_result.txt").readlines())
            #     # inset = open("Result_Domains_Added.txt", "+a")
            #     # inset.write(domainlist)
            #     # inset.close()
            #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ajaxfiles'))).click()
            #     time.sleep(10)
            #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#action-upload>a'))).click()
            #     pyautogui.write(pathfilehtml)
            #     pyautogui.press('enter')
            #     # htmlupload = driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
            #     # htmlupload.send_keys(pathfilehtml)
            #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="return-link"]//a[1]'))).click()
            #     content = driver.page_source
            #     result = content.find('index.html')
            #     print("Uploaded")
            #     driver.close()
            # else:
            #     print("Failed To Upload")
            #     driver.close()
        else:
            print("Failed To Add Domain")
            driver.close()
    else:
        print("Failed To Find Add Domain")
        driver.close()
    driver.close()




