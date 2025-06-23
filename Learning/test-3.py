import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

# Wait for and click search icon
wait = WebDriverWait(driver, 10)
searchIcon = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='flexR gs-toggle-icon']")))
searchIcon.click()

# Wait for search input and send keys
enterText = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='gs-input']")))
enterText.click()
enterText.send_keys("Data Structure")
enterText.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()

