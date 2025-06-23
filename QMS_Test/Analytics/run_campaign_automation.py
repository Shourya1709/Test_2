from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import login1

def run_campaign_automation():
    # Set up ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)

    # Call external login function
    login1.login(driver)
    check = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@title = "Select Date Campaign"]')))
    check.click()

    dc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Zomato SOS"]')))
    dc.click()
    

    # Navigate and interact with the page
    anal = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[2]/span'))
    )
    anal.click()
  

   
 
    time.sleep(1)

    # Click the Submit button
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # Return the driver for further use
    return driver
