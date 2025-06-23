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
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[4]/span').click()
time.sleep(2)
print(f"\n \n Waiting for Agent to be visible")
if "agent" in driver.current_url.lower():
    print("Successfully navigated to Agent Profile")
else:
    print("Failed to navigate to Agent Profile")
# Verify the title of the page
print("Current URL is:", driver.current_url)    
time.sleep(2)
driver.quit()