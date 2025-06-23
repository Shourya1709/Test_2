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

profile_icon = driver.find_element(By.XPATH, '//span[@aria-label="user"]') 
actions = ActionChains(driver)
actions.move_to_element(profile_icon).perform()
time.sleep(2)

# Wait for logout to be visible and click
wait = WebDriverWait(driver, 10)
logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Logout')]")))
logout_button.click()

time.sleep(4)
welc = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/div/h2')
text = welc.text
print("Checking if user has logged out........")
print()
if text == "Welcome Back": 
    print("Successfully Logged Out")
else :
    print("Log Out Failed")
driver.quit()



