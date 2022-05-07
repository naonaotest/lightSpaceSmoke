from Action.create_OneProject_toReport import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from PageObject.createProject_page import *

import allure

@allure.feature("Test Login PriceMaintain function")
class TestCreateOneProject:
    @allure.testcase("TestCase1:change VOLUME5A/S030UNVD835/22U/WH to 70")
    def test_createOneProject_successs(self):
        path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=path)
        global driver
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(2)

        login(driver, "testled007@hotmail.com", "Aa123456")

        createOneProjectToReport(driver)
        driver.implicitly_wait(2)

        assert_bestprice_eixst(driver)
