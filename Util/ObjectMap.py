#encoding=utf-8
from Util.Log import *
from selenium.webdriver.support.ui import WebDriverWait

# 获取单个页面元素对象
def find_element(driver, locateType, locatorExpression):
    try:
        element = WebDriverWait(driver, 5).until\
            (lambda x: x.find_element(by = locateType, value = locatorExpression))
        info(locatorExpression)
        return element
    except Exception as e:
        error(locatorExpression)
        raise e

# 获取多个相同页面元素对象，以list返回
def find_elements(driver, locateType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 5).until\
            (lambda x:x.find_elements(by = locateType, value = locatorExpression))
        return elements
    except Exception as e:
        raise e

if __name__ == '__main__':
    from ProjectVar.var import *
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver

    path = project_path+'\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(stg_server)
    driver.implicitly_wait(2)
    print(driver.title)
    find_element(driver,"id","normal_login_username1")
    driver.quit()




