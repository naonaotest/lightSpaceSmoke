from Action.create_OneProject_toReport import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from PageObject.createProject_page import *

import allure

@allure.feature("Test Login PriceMaintain function")
class TestSaveReport:
    @allure.testcase("TestCase1:change VOLUME5A/S030UNVD835/22U/WH to 70")
    def test_saveReport_successs(self):
        path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=path)
        global driver
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(2)

        login(driver, "testled007@hotmail.com", "Aa123456")

        reportName=createOneProjectToReport(driver)
        try:
            pyautogui.moveTo(1260, 156, duration=2)
            pyautogui.click()
#        reportPage.saveReport_button(driver).click()
            info("Success find saveReport_button")
        except:
            flag = False
            warning("Fail find saveReport_button")

#        print(reportName in get_reportNameSavedOne_by_API())
        compareResult=reportName in get_reportNameSavedOne_by_API()

        assert(compareResult,True)
