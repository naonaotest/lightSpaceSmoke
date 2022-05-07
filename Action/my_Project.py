from Action.login import *
import pyautogui
from PageObject.myProject_page import *
from Action.assert_button import *

def myProject(driver):
    MPJ=myProjectPage(driver)
    try:
        MPJ.myProjectBlock()
        info("Success find myProjectBlock")
    except:
        flag=False
        warning("Fail find myProjectBlock")

    print("****",MPJ.myProjectBlock())
    MPJ.myProjectBlock().click()
    driver.implicitly_wait(5)

    #edit button
#    pyautogui.moveTo(x=335, y=494)
#    time.sleep(2)
#    pyautogui.click()

    time.sleep(10)


    #delete button
    pyautogui.moveTo(x=385, y=499)
    time.sleep(2)
    pyautogui.click()
    driver.implicitly_wait(2)
    MPJ.ongoing_delete_confirmbutton().click()

#    assert (int(before_delete),1+int(after_delete))





if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(2)

    login(driver, "testled007@hotmail.com", "Aa123456")
    myProject(driver)