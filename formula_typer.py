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

