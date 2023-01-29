from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from get_data import Console
import time

username = "as2c-hcnm"

def login(username):
    try:
        nbox1 = driver.find_element(By.CSS_SELECTOR ,"body > div.pageWrapper.onDomAppend > div.scrollDiv.pageScrollWrapper.allowBackSwipe.onStatusBarTap > div.scrollDivContainer.onWindowResize.onDomRemove.onDomAppend > div > div > div:nth-child(2) > div.page > div > div:nth-child(1) > div:nth-child(1) > div > div.onSubscribeLogsDone.onNewLogEvents_setAvatar.onNewLogEvents_setName > div > div:nth-child(1)")
        nbox1.click()
        time.sleep(0.5)

        nbox2 = driver.find_element(By.CSS_SELECTOR, "body > div.pageWrapper.onDomAppend > div.scrollDiv.pageScrollWrapper.allowBackSwipe.onStatusBarTap > div.scrollDivContainer.onWindowResize.onDomRemove.onDomAppend > div > div > div:nth-child(2) > div.page > div:nth-child(1) > div.input > div.scroller > div.divEditable.divEditable03em15em.onSoftKeyboardHeightChange.onDomRemove")
        nbox2.send_keys(username)
        time.sleep(0.5)

        nbox3 = driver.find_element(By.CSS_SELECTOR, "body > div.pageWrapper.onDomAppend > div.scrollDiv.pageScrollWrapper.allowBackSwipe.onStatusBarTap > div.scrollDivContainer.onWindowResize.onDomRemove.onDomAppend > div > div > div:nth-child(2) > div.page > div:nth-child(1) > div.buttonsSubmitCancel > div")
        nbox3.click()
        time.sleep(0.5)

        nbox3 = driver.find_element(By.CSS_SELECTOR, "body > div.pageWrapper.onDomAppend > div.scrollDiv.pageScrollWrapper.allowBackSwipe.onStatusBarTap > div.scrollDivContainer.onWindowResize.onDomRemove.onDomAppend > div > div > div:nth-child(2) > div.page > div:nth-child(4) > div:nth-child(1)")
        nbox3.click()

        return True

    except: 
        return False

def initial_setup():
    # inital setup
    cn = Console()
    website = cn.inp("Input", "website url")

    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    try:
        driver.get(website)
    except:
        cn.write("Error", "invalid url trying default one...")
    try:
        driver.get("https://anton.app/")
    except:
        cn.write("Error", "conection error")


if __name__ == '__main__':
    initial_setup()
    time.sleep(2)
    login(username)

