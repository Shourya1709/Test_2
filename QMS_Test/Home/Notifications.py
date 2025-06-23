from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import login_auto

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

login_auto.login(driver)
time.sleep(8)


bell_icon = driver.find_element(By.XPATH, '//*[@class="anticon anticon-bell"]')
driver.execute_script("arguments[0].scrollIntoView(true);", bell_icon)
time.sleep(1)
bell_icon.click()
time.sleep(2)
# Clicking the first Notification and Verifying if it is NCSOS or SOS
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[1]/div/div/div/div[1]').click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div/div[2]/form/div/div[2]/div/div[2]/table/tbody/tr[7]/td[2]')))
Dispo = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div/div[2]/form/div/div[2]/div/div[2]/table/tbody/tr[7]/td[2]')
lead = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div/div[2]/form/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]')
print('For lead id - ',lead.text)
if Dispo.text == "SOS":
    print("It is a Compliant SOS Call")
else :
    print("It is not a Compliant SOS Call")
driver.close()
