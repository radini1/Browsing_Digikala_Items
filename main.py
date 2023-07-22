from selenium import webdriver as wd 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
import time 
import random 

wd = wd.Chrome()
wd.implicitly_wait(10)
wd.get('https://www.digikala.com/')

random_time_wait = random.randrange(5.0, 10.0)

search_place = wd.find_element(By.XPATH, '//*[@id="base_layout_desktop_fixed_header"]/header/div/div/div/div[1]/div/div/div[1]/div/span/div')
search_place.click()

time.sleep(random_time_wait)
searching = wd.find_element(By.XPATH, '//*[@id="base_layout_desktop_fixed_header"]/header/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/label/div/div/input')
searching.send_keys('samsung')
searching.send_keys(Keys.ENTER)

wd.get('https://www.digikala.com/search/?q=samsung')

time.sleep(random_time_wait)
wait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='پرفروش‌ترین‌']"))).click()
