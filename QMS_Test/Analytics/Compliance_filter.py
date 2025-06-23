from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import login1


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


login1.login(driver)
print(f"\n \n Waiting for Analytics to be visible")



wait = WebDriverWait(driver, 20)
el = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[2]/span')))
el.click()
check = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Analytics")]')))
 

sentiment = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div[3]')))
sentiment.click()


filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Select Date Range"]')))
filter.click()
date_filter = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title= "Current Day"]')))
#can change date filter to any option avaiable
date_filter.click()
time.sleep(20)
driver.quit()