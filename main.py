from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
stalker = webdriver.Chrome()
from datetime import datetime
import time
stalker.get("https://web.whatsapp.com")
sessionStart = None; 
checked = False;
sessions = [];

while True:
	try:
		name = stalker.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').text
		try:
			stalker.find_element_by_xpath('//*[@title="online"]')
			if(checked == False):
				sessionStart = time.time();
				checked = True
		except:
			if(sessionStart!=None):
				sessionEnd = datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')
				duration = int(time.time() - sessionStart)
				sessioStart = datetime.utcfromtimestamp(sessionStart).strftime('%H:%M:%S')
				# print(sessioStart, str(duration), sessionEnd)
				sessions.append([sessioStart, str(duration), sessionEnd])
				if(checked == True):			
					print("{}. {} opened whatsapp at {}, stayed for {} seconds and went offline on {}".format(len(sessions),name,sessions[-1][0],sessions[-1][1],sessions[-1][2]))
					checked = False;
				sessionStart = None
	except Exception as e:
		print(e,end = "\r")
		pass

		

