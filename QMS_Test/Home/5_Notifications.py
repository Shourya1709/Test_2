from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback
import login_auto

# Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Login
    login_auto.login(driver)

    wait = WebDriverWait(driver, 15)

    # Select campaign
    dc = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@title="Select Date Campaign"]')))
    dc.click()
    campaign = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Zomato SOS"]')))
    campaign.click()

    submit = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div/div[1]/div/form/div[3]/div/div/div/div'
    )))
    submit.click()

    # Wait for notification popup to disappear
    try:
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "ant-notification-notice"))
        )
    except:
        pass  # It's okay if it wasn't present

    # Click the bell icon
    bell_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//header//span/sup')))
    bell_icon.click()

    # Get list of notifications
    notif_list_xpath = '//ul[contains(@class,"ant-list-items")]/li'
    notif_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, notif_list_xpath)))

    print(f"\nFound {len(notif_elements)} notifications")

    for i, notif_element in enumerate(notif_elements[:5], start=1):
        try:
            print(f"\nChecking Notification #{i}")

            # Click the notification
            clickable = WebDriverWait(notif_element, 10).until(
                EC.element_to_be_clickable((By.XPATH, './div'))
            )
            clickable.click()

           
            dispo_xpath = (
                '//*[@id="root"]/div/div[1]/main/div/div/div/div[2]/form/div/div[2]/div/div[2]'
                '/table/tbody/tr[7]/td[2]'
            )
            lead_xpath = (
                '//*[@id="root"]/div/div[1]/main/div/div/div/div[2]/form/div/div[2]/div/div[2]'
                '/table/tbody/tr[3]/td[2]'
            )

            dispo = wait.until(EC.visibility_of_element_located((By.XPATH, dispo_xpath)))
            lead = wait.until(EC.visibility_of_element_located((By.XPATH, lead_xpath)))

            print("Lead ID:", lead.text.strip())
            if dispo.text.strip() == "SOS":
                print("It is a Compliant SOS Call")
            else:
                print("It is not a Compliant SOS Call")
            print("Disposition:", dispo.text.strip())
            time.sleep(2)

            

        except Exception as e:
            print(f"Error processing Notification #{i}:")
            traceback.print_exc()
            continue

except Exception as e:
    print("Unexpected error occurred:")
    traceback.print_exc()

finally:
    driver.quit()

