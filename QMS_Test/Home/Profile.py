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

# Hover over profile icon 
profile_icon = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/header/div/div[3]/div[2]') 
actions = ActionChains(driver)
actions.move_to_element(profile_icon).perform()
time.sleep(2)

wait = WebDriverWait(driver, 10)
Profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Profile")]')))
Profile_button.click()
time.sleep(2)
print(driver.title)
user = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/main/div/div/div[1]/div[1]/div/div[1]/div')
text = user.text
if text == "User Profile" :
    print("Successfully Reached User Profile Tab")
else : 
    print("Not Reached User Profile")

time.sleep(10)
driver.quit()