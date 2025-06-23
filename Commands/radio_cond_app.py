from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
searchbox = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input" )
print(print("Display Status : ",searchbox.is_displayed()))
print(print("Display Status : ",searchbox.is_enabled()))
time.sleep(2)
rd_male = driver.find_element(By.XPATH, "//*[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//*[@id='gender-female']")
time.sleep(1)
rd_male.click()

print(rd_male.is_selected())
print(rd_female.is_selected())
time.sleep(5)
driver.quit()