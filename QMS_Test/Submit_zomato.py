from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import login_auto

# Set up driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Perform login
login_auto.login(driver)
time.sleep(5)

S = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/span/span[2]')
S.click()
time.sleep(2)
wait = WebDriverWait(driver, 10)
el = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[contains(text(),"Zomato SOS")]')
))
el.click()
time.sleep(2)
submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div/form/div[3]/div/div/div/div/div/div/button/span')
time.sleep(1)
submit.click()
print(driver.title)

# bell_icon = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/header/div/div[3]/div[2]/span/sup')
# driver.execute_script("arguments[0].scrollIntoView(true);", bell_icon)
# time.sleep(1)
# bell_icon.click()
time.sleep(7)
driver.close()
