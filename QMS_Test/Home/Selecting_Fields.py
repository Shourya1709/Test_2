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
wait = WebDriverWait(driver, 10)


dropdown_button = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    '//div[.//span[text()="Select Date Campaign"] and contains(@class, "ant-select")]//div[contains(@class, "ant-select-selector")]'
)))
dropdown_button.click()

# Wait for the dropdown list to appear
wait.until(EC.visibility_of_element_located((
    By.CLASS_NAME,
    'ant-select-dropdown'
)))

el = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[contains(text(),"Zomato SOS")]')
))
el.click()


#Staus
driver.find_element(By.XPATH, '//*[@title = "Select status"]').click()
status = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Success"]')))
status.click()
#Call Duration

driver.find_element(By.XPATH, '//*[@title = "Select call duration"]').click()
call_dur = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Long"]')))
call_dur.click()


#Fatal/Non-fatal calls
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div/form/div[2]/div[5]/div/div/div[2]/div/div/div/div/span/span[2]').click()
time.sleep(0.5)
toc = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(), "Non Fatal Call")]')))
toc.click()
submit = driver.find_element(By.XPATH, '//*[@type="submit"]')
time.sleep(3)
submit.click()
print(driver.current_url)

# bell_icon = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/header/div/div[3]/div[2]/span/sup')
# driver.execute_script("arguments[0].scrollIntoView(true);", bell_icon)
# time.sleep(1)
# bell_icon.click()
time.sleep(7)
driver.close()


