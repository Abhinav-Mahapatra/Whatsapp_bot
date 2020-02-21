#
#Made by: Abhinav Mahapatra
#Contact : abhinav.mahapatra10@gmail.com
#
#
#This app is made solely for educational purposes and i will not be held responsibe/liable for any damage done by it
#
#
#

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random


class Whatsapp():
    def __init__(self, name, message, times):
        self.driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
        self.driver.get('https://web.whatsapp.com/')
        self.name = name
        self.message = message
        self.times = times

    def spam(self):
        # Putting the time.sleep in order to give the user enough time to scan
        time.sleep(10)

        # Searching the search bar for the name
        self.search = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input')
        self.search.click()
        self.search.send_keys(self.name + Keys.RETURN)
        time.sleep(3)

        
        for _ in range(self.times): 
            # Locating the message bar
            self.search = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div')
            self.search.click()
            self.search.send_keys(self.message + Keys.RETURN)
            # putting a random time gap between messages to avoid whatsapp detecting automation
            time.sleep(random.randint(0,3))



if __name__ =='__main__':

    print('=============----------------Welcome to the WhatsApp Silly_Spammer----------------=============')
    print('                                                                         -By Abhinav Mahapatra')
    # Getting the basic details
    name = input('Enter the Name: ')
    message = input('Enter the message: ')
    times = int(input('Enter the number of times you want to send the message: '))

    # Log into youtube
    obj = Whatsapp(name, message, times)
    obj.spam()
