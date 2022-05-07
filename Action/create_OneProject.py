import time

from Action.login import *
import pyautogui
from PageObject.createProject_page import *
from Action.assert_button import *
import pyautogui


def createOneProject(driver):
    createPro = CreateProjectPage(driver)
    try:
        createPro.createprojectblock().click()
        info("Success find createProjectBlock")
    except:
        flag = False
        warning("Fail find createProjectBlock")

    try:
        createPro.rectangle_button().click()
        info("Success find rectangle_button")
    except:
        flag = False
        warning("Fail find rectangle_button")

    pyautogui.click(510, 352, duration=2)
    pyautogui.click(986, 604, duration=2)
    pyautogui.click(600, 500, duration=2)
    time.sleep(2)

    try:
        pyautogui.click(1170, 352, duration=2)
#        createPro.zoneSettings_button().click()
        info("Success find zoneSettings_button")
    except:
        flag = False
        warning("Fail find zoneSettings_button")

    try:
        createPro.openWorkspace_button().click()
        time.sleep(3)
        info("Success find openWorkspace_button")
    except:
        flag = False
        warning("Fail find openWorkspace_button")

    try:
        createPro.intelligentDesign_button().click()
        time.sleep(5)
        driver.implicitly_wait(20)
        info("Success find intelligentDesign_button")
    except:
        flag = False
        warning("Fail find intelligentDesign_buttonk")

if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    login(driver, "testled007@hotmail.com", "Aa123456")
    createOneProject(driver)
    print("****")
