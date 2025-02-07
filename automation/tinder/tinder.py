'''
To login Tinder once then store the session, go to terminal:
'path/to/executable_chrome --remote-debugging-port=9222 --user-data-dir="path/to/profile_folder"'

To set automation, pip install pyinstaller.
cd to the python file directory:
'pyinstaller --onefile tinder.py'
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

SALUTATION = 'Hi!'
LIKE_ATTEMPTS = 20

path = 'path/to/chromedriver'
web = 'https://www.tinder.com'

options = Options()
options.add_experimental_option('debuggerAddress', 'localhost:9222')

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(web)
driver.maximize_window()

time.sleep(10) # wait 10s for page to load

for i in range(LIKE_ATTEMPTS):
    try:
        # xpath for like button: //button//span[text()="Like"]
        like_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button//span[text()="Like"]')))
        # like_button = driver.find_element(by='xpath', value='//button//span[text()="Like"]')
        # like_button.click()
        driver.execute_script('arguments[0].click();', like_button)
        time.sleep(1)

        # xpath for say sth nice when match: //textarea[@placeholder="Say something nice!"]
        popup_match = driver.find_element(by='xpath', value='//textarea[@placeholder="Say something nice!"]')
        popup_match.send_keys(SALUTATION)
        time.sleep(1)

        # Send button in match: //button[@data-testid="chatSendMessageButton"]
        send_message_match_button = driver.find_element(by='xpath', value=' //button[@data-testid="chatSendMessageButton"]')
        send_message_match_button.click()
        time.sleep(randint(1, 3))

        # Close button in match popup: //button[@title="Back to Tinder"]
        close_match_button = driver.find_element(by='xpath', value='//button[@title="Back to Tinder"]')
        close_match_button.click()
    except NoSuchElementException:
        try:
            # xpath for upgrade your like popup: //div[@data-testid="dialog"]//span[text()="No Thanks"]
            # Add Tinder to Home Screen popup: //div[@data-testid="dialog"]//span[text()="Not interested"]
            # uprade tinder gold, maybe later: //div[@data-testid="dialog"]//span[text()="Maybe later"]
            box = driver.find_element(by='xpath', 
                value='//div[@data-testid="dialog"]//span[text()="No Thanks"] | //div[@data-testid="dialog"]//span[text()="Not interested"] | //div[@data-testid="dialog"]//span[text()="Maybe later"]'
            )
            box.click()
        except NoSuchElementException:
            pass





