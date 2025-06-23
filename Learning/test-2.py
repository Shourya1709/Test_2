import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Launch undetected Chrome browser
drv = uc.Chrome()

# Open Google
drv.get("https://www.google.com")

# Search "GeeksforGeeks"
box = drv.find_element(By.NAME, "q")
box.send_keys("GeeksforGeeks", Keys.RETURN)

# Wait and close browser
time.sleep(5)
drv.quit()

