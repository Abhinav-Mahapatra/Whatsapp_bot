#
#Made by: Abhinav Mahapatra
#Contact : abhinav.mahapatra10@gmail.com
#
#
#This app is made solely for educational purposes and i will not be held responsibe/liable for any damage done by it
#
#
#

from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

    
def whtsapp_spam(target,message,times):
    #opening the browser and waiting for the login
    driver = webdriver.Chrome(r'C:\ChromeDriver\chromedriver.exe')
    driver.get("https://web.whatsapp.com/")
    time.sleep(20)

    #Search on the search-bar for the name of the person/group 
    elem = driver.find_element_by_xpath('html/body/div/div/div/div[2]/div[2]/div/label/input')
    elem.click()
    elem.send_keys(target + Keys.RETURN)
    time.sleep(2)

    
    #Goes into the bottom text bar and loops
    elem1 = driver.find_element_by_xpath('html/body/div[1]/div/div/div[3]/footer/div[1]/div[2]/div/div[2]')
    for _ in range(times):
        elem1.send_keys(message)
        time.sleep(1)
        button = driver.find_element_by_xpath('html/body/div[1]/div/div/div[3]/footer/div[1]/button')
        button.click()

    driver.quit()
    print('code completed')

if __name__ == '__main__':
    try:
        print('=============----------------Welcome to the WhatsApp Silly_Spammer----------------=============')
        print('                                                                         -By Abhinav Mahapatra')
        target = raw_input('Enter the name of friend/group: ')
        message = raw_input('Enter the Message: ')
        times = int(input('Enter the amount of times to loop: '))
        whtsapp_spam(target,message,times)
    except Exception as err:
        print('Invalid Entry')    
