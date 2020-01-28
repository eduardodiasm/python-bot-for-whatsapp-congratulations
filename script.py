from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://web.whatsapp.com/')

time.sleep(4)

people_names = ['person Name']

for person_name in people_names:
    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(person_name))
    person.click()
    for i in range(1, 3):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        messageContent = driver.find_elements_by_css_selector('span.selectable-text.invisible-space.copyable-text')
        message = [message.text for message in messageContent]
        # Replying in English
        if message[-1] == 'Happy birthday':
            reply = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
            reply.clear()
            reply.send_keys('Thank you :)')
            reply.send_keys(Keys.RETURN)

        # Replying in portuguese
        elif message[-1] == 'Feliz aniversário':
            reply = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
            reply.clear()
            reply.send_keys('Valeu, ', person_name, ' :)')
            reply.send_keys(Keys.RETURN)
            