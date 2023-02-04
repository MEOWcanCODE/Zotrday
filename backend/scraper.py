from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json

options = Options()
options.headless = True
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.get('https://www.lib.uci.edu/study-space-locator')

element = WebDriverWait(browser, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.study ')))

names = browser.find_elements(By.CSS_SELECTOR, 'li.study ')

for items in names:
    attributes = items.text.split('\n')
    str = (json.dumps({'Name': attributes[1], 'Location': attributes[2], 'Time':attributes[3]}))
    print(str)
    print()
