from selenium import webdriver
from selenium.webdriver.common.by import By

# inital setup
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://www.realmath.de/Neues/Klasse8/binome/binomevar03.php")