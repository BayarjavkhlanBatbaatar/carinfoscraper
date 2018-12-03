from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import selenium

import time
import csv
import json
from bs4 import BeautifulSoup
import sys

import pyscreenshot as ImageGrab
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import time
import os.path

# -*- coding: utf-8 -*-

file_id = 'smartcar'

def main():
	# Create a new instance of the Firefox driver
	reload(sys)
	sys.setdefaultencoding('utf-8')

	option = webdriver.ChromeOptions()
	option.add_argument('--incognito')

	driver = webdriver.Chrome(executable_path='/Users/bayarjavkhlan/Downloads/chromedriver', chrome_options=option)

	file = open('plateNumber', 'r') 
	plateNumberFile = file.read()
	plateNumberFile = plateNumberFile.split()

	file = open('%s_scrape.csv' % file_id, 'a')
	w = csv.writer(file)

	i = 1
	for plateNumber in plateNumberFile:
		# go to the google home page
		print("%s th plate number is being processed." % i)
		i = i+1
		driver.get("http://smartcar.mn")

		driver.find_element_by_xpath("""//*[@id="licensePlate"]""").click()
		username = driver.find_element_by_id("licensePlate")

		# print(plateNumber)

		username.send_keys(plateNumber.decode('utf-8'))

		# print("plate number should be filled")

		driver.find_element_by_xpath("""//*[@id="vehicleNumberForm"]/button""").click()

		time.sleep(1)
		im=ImageGrab.grab(bbox=(528,260,616,304)) # X1,Y1,X2,Y2
		catcha_key = pytesseract.image_to_string(im)
		# print(catcha_key)

		capcha = driver.find_element_by_xpath("""//*[@id="captcha"]/div[2]/input""")
		capcha.send_keys(catcha_key)
		# print("captcha should be filled")
		driver.find_element_by_xpath("""//*[@id="captcha"]/div[2]/button""").click()
		tryN = 1
		try:
		    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, """//*[@id="container-dashboard"]""")))
		except:
			pass
			tryN = 0
		    # print("Oops!  That was no valid number.  Try again...")
		# print("finished to wait")
		if tryN != 0:
			data = driver.find_element_by_xpath("""//*[@id="container-dashboard"]""")
			text = data.text
			# print(text)
			text = text.splitlines()
			w.writerow([text[1], text[2], text[3]])

if __name__ == "__main__":
    main()