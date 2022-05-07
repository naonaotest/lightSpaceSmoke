import Action.assert_button
from ProjectVar.var import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from Action.login import *
from PageObject.priceMantain_page import *
import allure

@allure.feature("Test Login function")
class TestLoginPage:
    @allure.testcase("TestCase1:LoginSuccess")
    def test_login_successs(self):
        path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=path)
        global driver
        driver= webdriver.Chrome(service=service, options=options)
        login(driver,"testled007@hotmail.com","Aa123456")
        info("*************")
        myPrice1=PriceMantainPage(driver)
        Action.assert_button.assert_element_exist(driver,myPrice1.priceMaintainBlock())

        driver.quit()

    @allure.testcase("TestCase2:Loginfail")
    def test_login_fail_withWrongPassWord(self):
        path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=path)
        global driver
        driver= webdriver.Chrome(service=service, options=options)
        login(driver,"testled007@hotmail.com","Aa1234567")
        lp1=LoginPage(driver)
        driver.implicitly_wait(2)
        info("*************")
        Action.assert_button.assert_element_exist(driver,lp1.username())
        driver.quit()