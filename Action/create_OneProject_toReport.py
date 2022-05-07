import time

from Action.login import *
import pyautogui
from PageObject.createProject_page import *
from Action.create_OneProject import *
from Action.assert_button import *
import pyautogui
from Util.FormatTime import *

def createOneProjectToReport(driver):
#    createPro = CreateProjectPage(driver)

    createOneProject(driver)

    try:
        pyautogui.moveTo(541,144,duration=2)
        pyautogui.click()
#        createPro.afterIntelligentSave_button().click()
        driver.implicitly_wait(2)
        info("Success find afterIntelligentSave_button")
    except:
        flag = False
        warning("Fail find afterIntelligentSave_button")


    global projectname
    projectname= time_to_name()

    try:
        pyautogui.moveTo(585,371,duration=2)
        pyautogui.click()
#        global projectname


        pyautogui.typewrite(projectname)

        time.sleep(5)


#        createPro.projectName_button().sendkeys(projectname)
        info("Success find projectName_button")
    except:
        flag = False
        warning("Fail find projectName_button")

    pyautogui.moveTo(791,431,duration=2)
    pyautogui.click()
    time.sleep(10)

    try:
        CreateProjectPage(driver).viewFullReport_button().click()
        info("Success find viewFullReport_button")
    except:
        flag = False
        warning("Fail find viewFullReport_button")

    try:
        CreateProjectPage(driver).bestprice_button()
        info("Success find bestprice_button")
    except:
        flag = False
        warning("Fail find bestprice_button")


    return(projectname)









if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    login(driver, "testled007@hotmail.com", "Aa123456")
    createOneProjectToReport(driver)
    print("****")