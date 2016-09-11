from bs4 import BeautifulSoup
from os import system
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_wa = webdriver.Chrome()
driver_wa.get('https://web.whatsapp.com/')

driver_bot = webdriver.PhantomJS()
driver_bot.set_window_size(1280, 1024)
driver_bot.get('http://www.cleverbot.com/')
sleep(15)
clever_bot = driver_bot.find_element_by_class_name('stimulus') 

driver_box = driver_wa.find_element_by_xpath('.//div[@class = "input"]')


pre_cont = "Start"
cont = ""
content = ""

while(True):
	url = driver_wa.page_source
	soup = BeautifulSoup(url,"html.parser")
	post_content = soup.findAll('span',{'class' : 'emojitext selectable-text'})

	last_div = None
	for last_div in post_content:
		pass

	if last_div:
		content = last_div.getText()

	if content == pre_cont:
		flag = False
	else:
		pre_cont = content
		flag = True
    	


	if flag:
		clever_bot.send_keys(content)
		clever_bot.send_keys(Keys.RETURN)
		sleep(3)
		for elem in driver_bot.find_elements_by_xpath('.//span[@class = "bot"]'):
			cont = elem.text
		pre_cont = cont
		driver_box.send_keys(cont)

		

	sleep(20)



