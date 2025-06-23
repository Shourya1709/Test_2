# Import required modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()

# Set up Chrome service using ChromeDriverManager
service = Service(ChromeDriverManager().install())

# Create the driver object
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Google
    driver.get("https://www.google.com")
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
