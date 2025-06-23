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



wait = WebDriverWait(driver, 25)
check = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Select Date Campaign"]')))
check.click()

dc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Zomato SOS"]')))
dc.click()
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(5)

el = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[2]/span')))
el.click()
check = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Analytics")]')))
 

sentiment = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div[3]')))
sentiment.click()


tot = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='compliance-card-content'][.//h4[text()='Total SOS Calls']]")))
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", tot)
tot.click()
if "Total" in driver.current_url:
    print("Total SOS button is working")
else:
    print("Total SOS button does not work")
driver.back()

csos = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='compliance-card-content'][.//h4[text()='Compliant SOS Calls']]")))
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", csos)
csos.click()
if "Compliant" in driver.current_url:
    print("Compliant SOS button is working")
else:
    print("Compliant SOS button does not work")
driver.back()

ncsos = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='compliance-card-content'][.//h4[text()='Non-Compliant SOS Calls']]")))
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ncsos)
ncsos.click()

if "Non-Compliant" in driver.current_url:
    print("Non-Compliant SOS button is working")
else :
    print("Non-Compliant SOS button does not work")
driver.back()
time.sleep(2)
driver.quit()