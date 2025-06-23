from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://172.20.51.11:8000/qmsui/login")
driver.maximize_window()


time.sleep(1)
email_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div[2]/div/form/div[1]/div/div[2]/div/div/span/input" ))
)
email_input.send_keys("shourya.sharma@radicalminds.co")

time.sleep(1)
driver.find_element(By.ID, "password").send_keys("12aa12aa")
time.sleep(1)
driver.find_element(By.XPATH, "//button[span[text()= 'Log In']]").click()

time.sleep(5)
act_title = driver.title
time.sleep(1)
print(act_title)
"""exp_title = ""
time.sleep(1)
print(exp_title)
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.quit()
"""






