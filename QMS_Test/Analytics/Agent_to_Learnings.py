#driver.find_element(By.XPATH, '//*[text()="Learnings"]').click()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import login1
import run_campaign_automation




driver = run_campaign_automation.run_campaign_automation()
agent = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/main/div/div/div[1]/div[2]')
agent.click()
time.sleep(1)
wait = WebDriverWait(driver, 10)
learnings = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/button[2]')))
learnings.click()
if "learning" in driver.current_url:
    print("Learnings page opened successfully.")
else:
    print("Failed to open Learnings page.")



time.sleep(5)
driver.quit()