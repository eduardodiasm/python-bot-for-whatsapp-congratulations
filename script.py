from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://web.whatsapp.com/')

input('press any key after QR scan ')
time.sleep(4)

people_names = ['personName']

for person_name in people_names:
    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(person_name))
    person.click()
    for i in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")