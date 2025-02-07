'''
Remember to pip install pyinstaller.
Then run 'pyinstaller --onefile news.py' in the terminal
to generate execution file (the file is in dist folder).
To set exe file runs automatically daily, try this:

MAC
'crontab -e' to open new terminal window,
press I to set INSERT mode then input '0 9 * * * {file_path}',
then press K,
then type ':wq'

PC
create a txt file then input:
"path\to\python.exe" "path\to\my_script.py"
then save it as .bat file.
Search for Task Scheduler app on windows > Create Basic Task
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options # set options for selenium behaviour
from selenium.webdriver.chrom.service import Service
import pandas as pd
# libraries for automation
from datetime import datetime
import os, sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()
date_export = now.strftime('%a_%Y%m%d')

website = "https://machinelearningmastery.com/10-must-know-python-libraries-for-machine-learning-in-2024/"
path = '' # Path of Chrome Driver downloaded on local disk

# headless mode
options = Options()
options.headless = True # headless=True means it doesn't open the website after the task finishes

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

# find_elements return a list
# find_elemnt return a value
containers = driver.find_elements(by='xpath', value='//div[@class="dfgdger"]')

articles = []

for container in containers:
    title = container.find_element(by='xpath', value='./a.h2').text
    subtitle = container.find_element(by='xpath', value='./a.p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')

    articles.append([title, subtitle, link])

file_name = f'article_{date_export}.csv'
file_path = os.path.join(app_path, file_name)

pd.DataFrame(articles, columns=['Title', 'Subtitle', 'Link'])\
    .to_csv(file_path, index=False)

driver.quit()