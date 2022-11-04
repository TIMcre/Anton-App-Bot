from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from get_data import Console

cn = Console()
website = str(input("website url"))
# inital setup
s = Service("geckodriver.exe")
driver = webdriver.Firefox(service=s)

try:
    driver.get(website)
except:
    console.write("Error", "invalid url trying default one...")
    try:
        driver.get("https://anton.app/de/")
    except:
        console.write("Error", "conection error")
nbox1 = driver.find_element(By.CSS_SELECTOR,"/html/body/div[5]/div[4]/div/div[3]/div[1]")
ibox = driver.find_element(By.CSS_SELECTOR,"/html/body/div[5]/div[4]/div/div[3]/div[1]")
while True:
    print(test)
    try:
        
        nbox1.click        
        ibox.click()
        print("fslklf")
    except:
        pass

