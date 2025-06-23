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
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[2]/span').click()
time.sleep(2)
print(f"\n \n Waiting for Analytics to be visible")
wait = WebDriverWait(driver, 10)
check = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Analytics")]')))
if check:
    print("Successfully navigated to Analytics")
else:
    print("Failed to navigate to Analytics")
# Verify the title of the page

print("Current URL is:", driver.current_url)
if "analytics" in driver.current_url.lower():
    print("URL is correct, contains 'analytics'")
else:
    print("URL is incorrect, expected 'analytics' in URL")
print(f"\n\nAnalytics->Compliance............")  

sentiment = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div[3]')))
sentiment.click()
time.sleep(5)
if "compliance" in driver.current_url.lower():
    print("Successfully navigated to Compliance from Analytics")
else:
    print("Failed to navigate to Compliance from Analytics")    
time.sleep(2)
print(f"\n\n Home->Analytics->Compliance is successful")

driver.quit()