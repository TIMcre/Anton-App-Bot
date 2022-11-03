from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

website = str(input("website url"))
# inital setup
s = Service("geckodriver.exe")
driver = webdriver.Firefox(service=s)
try:
    driver.get(website)
except:
    print("invalid url trying default one...")
    try:
        driver.get("https://anton.app/de/")
    except:
        print("conection error")

while True:
    print(test)
    try:
        nbox1 = driver.find_element(By.CSS_SELECTOR,"/html/body/div[5]/div[4]/div/div[3]/div[1]")
        nbox1.click
        nbox2 = driver.find_element(By.CSS_SELECTOR,"/html/body/div[5]/div[4]/div/div[3]/div[2]")
        nbox2.click
        ibox = driver.find_element(By.CSS_SELECTOR,"/html/body/div[5]/div[4]/div/div[3]/div[1]")
        ibox.click()
        print("fslklf")
    except:
        pass