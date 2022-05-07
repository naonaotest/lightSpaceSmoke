from Action.assert_button import get_reportsNumber_by_API
from Action.my_Report import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from PageObject.priceMantain_page import *

import allure

@allure.feature("Test Login PriceMaintain function")
class TestReportPage:
    @allure.testcase("TestCase1:change VOLUME5A/S030UNVD835/22U/WH to 70")
    def test_report_successs(self):
        path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=path)
        global driver
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(2)

        login(driver, "testled007@hotmail.com", "Aa123456")

        before_delete = get_reportsNumber_by_API()
        print(type(before_delete))
        my_report(driver)
        after_delete = get_reportsNumber_by_API()
        print(type(after_delete))

        assert (int(before_delete), 1 + int(after_delete))