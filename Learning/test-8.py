import requests as request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.save_screenshot("screenshot.png")

alllinks = driver.find_elements(By.TAG_NAME, "a")
count =0

for link in alllinks:
    url = link.get_attribute("href")
    try : 

        res = request.get(url)
    except : 
        None
    
    
    if res.status_code >= 400:
        print(url , "is a broken link")
        count += 1
    else : 
        print(url, "is a valid link")
        
print("Total broken links are : ", count)
driver.quit()

