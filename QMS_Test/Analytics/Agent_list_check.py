from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import login1
import run_campaign_automation


def select_agent(driver, agent_name):
    wait = WebDriverWait(driver, 20)

    # Get the scrollable container
    container = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[contains(@class, "rc-virtual-list-holder-inner")]')
    ))

    attempts = 0
    found = False

    while attempts < 10:
        options = driver.find_elements(By.XPATH, '//div[contains(@class, "ant-select-item-option-content")]')
        for option in options:
            if option.text.strip().lower() == agent_name.strip().lower():
                option.click()
                found = True
                break

        if found:
            break

        driver.execute_script("arguments[0].parentElement.scrollTop += 100", container)
        time.sleep(0.5)
        attempts += 1

    if not found:
        print(f"Agent '{agent_name}' not found.")

driver = run_campaign_automation.run_campaign_automation()
agent = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/main/div/div/div[1]/div[2]')
agent.click()
time.sleep(5)
wait = WebDriverWait(driver, 20)
select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Select"]')))
select.click()
select_agent(driver, 'Saniya')  
#can change the agent name above to any agent name present in the list
# can shorten list by send keys

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div/div[1]/div/div/button[1]').click()
time.sleep(5)
driver.quit()