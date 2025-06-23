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



wait = WebDriverWait(driver, 20)
el = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[2]/span')))
el.click()
check = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Analytics")]')))
 

sentiment = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div[3]')))
sentiment.click()
hide = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label = "caret-up"]')))
hide.click()

Sos = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]/div[4]/div/div[3]/div[2]')))
Sos.click()
if "SOS" in driver.current_url:
    print("SOS Call button is working")
else: 
    print("Yikes !")
driver.back()
csos = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div/div[3]/div/div[1]/div/div[5]/div/div[3]/div[2]/span')))
csos.click()
if "Compliant" in driver.current_url:
    print("Compliant SOS Call button is working")
else: 
    print("Yikes ! Compliant SOS Call button is not working")
driver.back()
ncsos = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div/div[3]/div/div[1]/div/div[6]/div/div[3]/div[2]/span')))
ncsos.click()
if "Non-Compliant" in driver.current_url:
    print("NCSOS Button is working")
else : 
    print("Yikes ! NCSOS Button is not working ")

driver.quit()