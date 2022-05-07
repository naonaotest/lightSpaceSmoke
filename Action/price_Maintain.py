from PageObject.priceMantain_page import *
from Action.login import *
import pyautogui



def PriceMaintan(driver,value1,value2):
    PM = PriceMantainPage(driver)
    try:
        PM.priceMaintainBlock().click()
        driver.implicitly_wait(2)
        info("Success find priceMaintainBlock button")
    except Exception as e:
        warning("Fail find priceMaintainBlock button")
        error(e)
#    driver.switch_to().frame("frame")

    try:
        pyautogui.moveTo(x=1318, y=481)
        time.sleep(1)
        pyautogui.click()
        info("Success find Edit button")
    except Exception as e:
        warning("Fail find Edit button")
        error(e)
#    PM.priceMaintainEditButton().click()

    time.sleep(2)
    try:
        webdriver.ActionChains(driver).double_click(PM.priceMaintainChange1Box()).perform()
        time.sleep(2)
        PM.priceMaintainChange1Box().send_keys(value1)
        info("Success find value1 button")
    except Exception as e:
        warning("Fail find value1 button")
        error(e)

    try:
        webdriver.ActionChains(driver).double_click(PM.priceMaintainChange2Box()).perform()
        PM.priceMaintainChange2Box().send_keys(value2)
        info("Success find value2 button")
    except Exception as e:
        warning("Fail find value2 button")
        error(e)


    try:
        PM.priceMaintainConfirmButton().click()
        info("Success save price button")
    except Exception as e:
        warning("Fail save price button")
        error(e)



if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    login(driver, "testled007@hotmail.com", "Aa123456")
    PriceMaintan(driver,70,80)


