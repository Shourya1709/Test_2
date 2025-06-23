import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = uc.Chrome()

# Open Amazon
driver.get("https://amazon.in")
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.back()
time.sleep(1.5)
driver.forward()
driver.refresh()

time.sleep(3)
