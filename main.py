
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

stalker = webdriver.Chrome()
import time
from datetime import datetime
import time
stalker.get("https://web.whatsapp.com")

input()

while True:

	try:	
		stalker.find_element_by_xpath('//*[@title="online"]')
		print("Aditi was online on ")
		print(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		time.sleep(5)
		
	except:
		print("Aditi went offline on ")
		print(datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		time.sleep(5)
		

		

