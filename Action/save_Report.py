###could delete this py

from Action.create_OneProject_toReport import *
from PageObject.report_Page import *
from Action.assert_button import *
import pyautogui
from Util.FormatTime import *





def saveReport(driver):
    AAA=createOneProjectToReport(driver)
    try:
        pyautogui.moveTo(1260, 156, duration=2)
        pyautogui.click()
#        reportPage.saveReport_button(driver).click()
        info("Success find saveReport_button")
    except:
        flag = False
        warning("Fail find saveReport_button")

    print(AAA in get_reportNameSavedOne_by_API())
    ttt=AAA in get_reportNameSavedOne_by_API()

    assert(ttt,True)


if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    login(driver, "testled007@hotmail.com", "Aa123456")
    saveReport(driver)

    print("****")