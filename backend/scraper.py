from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json


options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.get('https://www.lib.uci.edu/study-space-locator')

element = WebDriverWait(browser, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.study ')))

click_button = browser.find_element(By.ID, "f_submit")
click_button.click()
names = browser.find_elements(By.CSS_SELECTOR, 'li.study ')


study_list = {}
for items in names:
    id_num = items.get_attribute("id")
    attributes = items.text.split('\n')
    if attributes[3] == "today:":
        attributes[3] = "Hours not listed"
    study_list[id_num] = {'Name': attributes[1], 'Location': attributes[2], 'Time':attributes[3], 'Image-URL':"", 'Amenities':[]}

src = browser.find_elements(By.XPATH,"//img[contains(@class,'center-image image-responsive')]")
img_list = []
for items in src:
    img_list.append(items.get_attribute("src"))
i = 0
for spot in study_list:
    study_list[spot]['Image-URL'] = img_list[i]
    str = json.dumps(study_list[spot])
    print(str)
    print()
    i += 1
