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

src = browser.find_elements(By.XPATH,"//img[contains(@class,'center-image image-responsive')]")
for items in src:
    print(items.get_attribute("src"))



amenities_lst = browser.find_elements(By.CLASS_NAME, "amenities-icon")
for icons in amenities_lst:
    amenity = icons.get_attribute('class')[21:]
    print("Amenity: ", amenity)

    div_class = icons.find_element(By.XPATH, "..")
    parent = div_class.find_element(By.XPATH, "..")

    parent_id = parent.get_attribute("id")
    print("Parent class attribute:", parent_id)
    


for items in names:
    attributes = items.text.split('\n')
    str = (json.dumps({'Name': attributes[1], 'Location': attributes[2], 'Time':attributes[3]}))
    print(str)
    print()
