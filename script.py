from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://web.whatsapp.com/')

input('press any key after QR scan ')
