from main import *

initial_setup()
time.sleep(2)
while not login:
    pass
while True:
    try:
        input_box_1 = driver.find_element(By.CSS_SELECTOR, "")
        time.sleep(0.5)
        input_box_1.send_keys("test")
    except:
        pass
    print("k")

    
   