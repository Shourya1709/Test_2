from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import login_auto

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

login_auto.login(driver)

time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
driver.refresh()

driver.quit()