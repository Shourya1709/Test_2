from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import login_auto

# Set up driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Perform login
login_auto.login(driver)
wait = WebDriverWait(driver, 10)
dc = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@title="Select Date Campaign"]')))
dc.click()
campaign = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Zomato SOS"]')))
campaign.click()




driver.find_element(By.XPATH, '//*[@title = "Select status"]').click()
status = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title = "Success"]')))
status.click()
submit = driver.find_element(By.XPATH, '//*[@type="submit"]')

submit.click()
time.sleep(3)
#first = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div')))
first = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[3]/span')))

first.click()
videos = driver.find_elements(By.TAG_NAME, 'video')
print("Number of <video> tags found:", len(videos))
for idx, video in enumerate(videos, start=1):
    print(f"Video #{idx}: src = {video.get_attribute('src')}")

time.sleep(5)

# try:
#     wait = WebDriverWait(driver, 10)
#     pause_icon = wait.until(EC.presence_of_element_located(
#         (By.XPATH, '//svg[@data-icon="pause-circle"]')
#     ))
#     print(" Audio is playing.")
# except:
#     print(" Audio is not playing.")
# time.sleep(2)
#this opens the first call details (Call Quality Audit)
#can be changed for tr[2]/td[3] -> 2nd call  //*[@id="root"]/div/div[1]/main/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[3]/span
driver.quit()
