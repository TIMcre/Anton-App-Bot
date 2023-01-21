from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from get_data import Console
import time

cn = Console()
website = cn.inp("Input", "website url")

# inital setup
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

try:
    driver.get(website)
except:
    cn.write("Error", "invalid url trying default one...")
    try:
        driver.get("https://anton.app/de/")
    except:
        cn.write("Error", "conection error")


while True:
    pass
   