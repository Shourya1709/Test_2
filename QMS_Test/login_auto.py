from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(driver):
    driver.get("http://172.20.51.13/qmsui/login")
    driver.maximize_window()
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div/div[1]/div[2]/div/form/div[1]/div/div[2]/div/div/span/input"))
    )
    email_input.send_keys("shourya.sharma@radicalminds.co")
    driver.find_element(By.ID, "password").send_keys("12aa12aa")
    driver.find_element(By.XPATH, "//button[span[text()= 'Log In']]").click()
