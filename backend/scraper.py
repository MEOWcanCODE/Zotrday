from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.get('https://www.lib.uci.edu/study-space-locator')

element = WebDriverWait(browser, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.study ')))

click_button = browser.find_element(By.ID, "f_submit")
click_button.click()
names = browser.find_elements(By.CSS_SELECTOR, 'li.study ')





