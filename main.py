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