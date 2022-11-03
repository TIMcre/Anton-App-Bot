from selenium import webdriver
from selenium.webdriver.common.by import By

website = str(input("website url"))
# inital setup
driver = webdriver.Firefox(executable_path="geckodriver.exe")
try:
    driver.get(website)
except:
    print("invalid url")