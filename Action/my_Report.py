from PageObject.myReport_page import *
from Action.login import *
import pyautogui
from PageObject import myProject_page


def my_report(driver):
    my_report=MyReport_Page(driver)
    my_report.my_report_Block().click()
    driver.implicitly_wait(10)
    pyautogui.moveTo(x=144, y=623)
    time.sleep(2)
    pyautogui.click()
    my_report.my_report_deleteConfirm_Button().click()



if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    login(driver, "testled007@hotmail.com", "Aa123456")
    my_report(driver)
    print("****")
