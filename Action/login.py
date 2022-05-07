from PageObject.login_page import *
from ProjectVar.var import *

def login(driver,username, password):
    driver.set_window_position(x=-8, y= -8)
    driver.set_window_size(width=1382, height=744)
    driver.get(stg_server)
    driver.implicitly_wait(5)
    lp = LoginPage(driver)

    try:
        lp.username().send_keys(username)
        info("Success find UserName button")
    except Exception as e:
        warning("Fail find UserName button")
        error(e)

    try:
        lp.password().send_keys(password)
        info("Success find PassWord button")
    except Exception as e:
        warning("Fail find PassWord button")
        error(e)

    try:
        lp.loginbutton().click()
        driver.implicitly_wait(2)
        info("Success find Login button")
    except Exception as e:
        warning("Fail find Login button")
        error(e)


if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
#    driver.get("https://www.ledvancels.com/#/")
#    driver.implicitly_wait(2)
    login(driver, "testled007@hotmail.com", "Aa123456")
