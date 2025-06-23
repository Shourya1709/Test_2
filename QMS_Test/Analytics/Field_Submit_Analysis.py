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
time.sleep(3)


driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/aside/div[1]/ul/li[2]/span').click()
time.sleep(2)
wait = WebDriverWait(driver, 10)
check = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Select Date Campaign"]')))
check.click()
dc = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Zomato SOS"]')))
dc.click()
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(20)
driver.close()

