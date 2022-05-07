import Action.assert_button
from ProjectVar.var import *
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from Action.login import *
from Action.price_Maintain import *
from PageObject.priceMantain_page import *
from Action.assert_button import *
import allure

@allure.feature("Test Login PriceMaintain function")
class TestPriceMaintainPage:
    @allure.testcase("TestCase1:change VOLUME5A/S030UNVD835/22U/WH to 70")
    def test_priceMaintain_successs(self):
        path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
        options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=path)
        global driver
        driver = webdriver.Chrome(service=service, options=options)
        login(driver, "testled007@hotmail.com", "Aa123456")
        PriceMaintan(driver, 70, 80)
        assert_price_Maintain_by_API("VOLUME5A/S030UNVD835/22U/WH", "70.00")
        driver.quit()
#        myPrice1 = PriceMantainPage(driver)
