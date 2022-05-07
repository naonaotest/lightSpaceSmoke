import time

from Action.login import *
import pyautogui
from PageObject.createProject_page import *
from Action.assert_button import *
import pyautogui

def setZoneSettings(position,function):
    pass


def createServelSpaceProject(driver):
    createPro = CreateProjectPage(driver)
    try:
        createPro.createprojectblock().click()
        info("Success find createProjectBlock")
    except:
        flag = False
        warning("Fail find createProjectBlock")

    pyautogui.click(510, 352, duration=2)
    time.sleep(5)
    pyautogui.scroll(-1000)
    pyautogui.click(510, 400, duration=2)
    pyautogui.scroll(-1000)
    time.sleep(5)

    try:
        createPro.rectangle_button().click()
        info("Success find rectangle_button")
    except:
        flag = False
        warning("Fail find rectangle_button")
    pyautogui.click(302, 197, duration=2)
    pyautogui.click(516, 466, duration=2)
    time.sleep(1)

    try:
        createPro.rectangle_button().click()
        info("Success find rectangle_button")
    except:
        flag = False
        warning("Fail find rectangle_button")
    pyautogui.click(516, 197, duration=2)
    pyautogui.click(787, 466, duration=2)
    time.sleep(1)

    try:
        createPro.rectangle_button().click()
        info("Success find rectangle_button")
    except:
        flag = False
        warning("Fail find rectangle_button")
    pyautogui.click(302,466, duration=2)
    pyautogui.click(886, 661, duration=2)
    time.sleep(1)

    try:
        createPro.irregular_button().click()
        info("Success find irregular_button")
    except:
        flag = False
        warning("Fail find irregular_button")
    pyautogui.click(780, 200, duration=2)
    pyautogui.click(1120, 343, duration=2)
    pyautogui.click(871, 505, duration=2)
    pyautogui.press('ESC')
    time.sleep(1)

    createPro.irregular_button().click()
    pyautogui.click(1107, 358, duration=2)
    pyautogui.click(1136, 583, duration=2)
    pyautogui.click(1096, 681, duration=2)
    pyautogui.click(869, 658, duration=2)
    pyautogui.press('ESC')
    time.sleep(1)

    createPro.subzone_button().click()
    pyautogui.click(332, 245, duration=2)
    pyautogui.click(455, 405, duration=2)
    time.sleep(1)

    createPro.subzone_button().click()
    pyautogui.click(809, 296, duration=2)
    pyautogui.click(903, 332, duration=2)
    time.sleep(1)

    createPro.subzone_button().click()
    pyautogui.click(816, 351, duration=2)
    pyautogui.click(971, 425, duration=2)
    time.sleep(1)

    createPro.subzone_button().click()
    pyautogui.click(322, 489, duration=2)
    pyautogui.click(415, 603, duration=2)
    time.sleep(1)

    createPro.subzone_button().click()
    pyautogui.click(453, 477, duration=2)
    pyautogui.click(609, 636, duration=2)
    time.sleep(1)

    createPro.subzone_button().click()
    pyautogui.click(553, 504, duration=2)
    pyautogui.click(795, 615, duration=2)
    time.sleep(1)














if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    login(driver, "testled007@hotmail.com", "Aa123456")
    createServelSpaceProject(driver)
    print("****")