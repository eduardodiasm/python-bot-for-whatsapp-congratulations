from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://web.whatsapp.com/')

input('Press something after the qr code page ')

# Fill this list with the name of your contacts (string format).
people_names = ['person one name example', 'person two name example']

for person_name in people_names:
    person = driver.find_element_by_xpath('//span[@title="{}"]'.format(person_name))
    person.click()
    for i in range(1, 3):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        messageContent = driver.find_elements_by_css_selector('span.selectable-text.invisible-space.copyable-text')
        message = [message.text for message in messageContent]
        # Replying in English
        if 'Happy birthday' in message[-1]:
            reply = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
            reply.clear()
            reply.send_keys('Thank you, ', person_name, ' :)')
            reply.send_keys(Keys.RETURN)

        # Replying in portuguese
        elif 'feliz aniversário' in message[-1].lower() or 'parabéns' in message[-1].lower():
            reply = driver.find_element_by_class_name('_3u328.copyable-text.selectable-text')
            reply.clear()
            reply.send_keys('Obrigado, ', person_name, ' :)')
            reply.send_keys(Keys.RETURN)
            
