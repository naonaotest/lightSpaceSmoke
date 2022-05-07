import pyautogui
from PageObject.createProject_page import *
from Action.create_OneProject import *
from Action.create_OneProject_toReport import *
from Action.login import *
import requests
def assert_element_exist(driver,find_element):
    try:
        find_element
    except Exception as e:
        return False
    else:
        return True

#def assert_price_Maintain(driver,lightname):
#    asPM=CreateProjectPage(driver)
#    asPM.myprojectblock().click()
#    driver.implicitly_wait(2)
#    try:
#        pyautogui.moveTo(x=20, y=513)
#        time.sleep(1)
#        pyautogui.click()
#        info("Success find Edit button")
#    except Exception as e:
#        warning("Fail find Edit button")
#        error(e)
#    asPM.light_productname_button().send_keys(lightname)
#    driver.implicitly_wait(2)
#    asPM.light_price_text().click()

def assert_price_Maintain_by_API(assertlight,assertprice):
    r_login=requests.post(url="https://www.ledvancels.com//api//app//account//user-login",
                   params={"username":"grace22712",
                           "password":"afdd0b4ad2ec172c586e2150770fbf9e"},
                   headers={"Authorization":"Basic c2FiZXI6c2FiZXJfc2VjcmV0"},
                   verify=False
                   ).json()
    token=r_login["access_token"]
    print("Bearer "+token)
    r_getprice=requests.get(url="https://www.ledvancels.com//api//app//product//list",
                            params={"current":1,
                                    "size":20,
                                    "keyword":assertlight},
                            headers={"Blade-Auth":"Bearer "+token},
                            verify = False).json()
    value=r_getprice['data']['records'][1]['price']
    info("light value is "+value)
    assert(assertprice=="70.00")

def get_projectsNumber_by_API():
    r_login = requests.post(url="https://www.ledvancels.com//api//app//account//user-login",
                            params={"username": "grace22712",
                                    "password": "afdd0b4ad2ec172c586e2150770fbf9e"},
                            headers={"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0"},
                            verify=False
                            ).json()
    token = r_login["access_token"]
    projects_number = requests.get(url="https://www.ledvancels.com//api/app/project/project-list",
                              params={"status": 0,
                                      "keyword": "",
                                      "current": 1,
                                      "size":0},
                              headers={"Blade-Auth": "Bearer " + token},
                              verify=False).json()
    return projects_number['data']['total']

def get_reportsNumber_by_API():
    r_login = requests.post(url="https://www.ledvancels.com//api//app//account//user-login",
                            params={"username": "grace22712",
                                    "password": "afdd0b4ad2ec172c586e2150770fbf9e"},
                            headers={"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0"},
                            verify=False
                            ).json()
    token = r_login["access_token"]
    reports_number = requests.get(url="https://www.ledvancels.com//api/app/project/report-list",
                              params={"keyword": "",
                                      "current": 1,
                                      "size":12},
                              headers={"Blade-Auth": "Bearer " + token},
                              verify=False).json()
    return reports_number['data']['total']

def assert_bestprice_eixst(driver):
    try:
        CreateProjectPage(driver).bestprice_button()
        info("Success find bestprice_button")
    except:
        flag = False
        warning("Fail find bestprice_button")


def get_reportNameSavedOne_by_API():
    r_login = requests.post(url="https://www.ledvancels.com//api//app//account//user-login",
                            params={"username": "grace22712",
                                    "password": "afdd0b4ad2ec172c586e2150770fbf9e"},
                            headers={"Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0"},
                            verify=False
                            ).json()
    token = r_login["access_token"]
    reports_number = requests.get(url="https://www.ledvancels.com//api/app/project/report-list",
                              params={"keyword": "",
                                      "current": 1,
                                      "size":12},
                              headers={"Blade-Auth": "Bearer " + token},
                              verify=False).json()
    recordlist= reports_number['data']['records']
    report_total_name=[]
    for i in recordlist:
        report_total_name.append(i["name"])
#    print(report_total_name[0])
    return report_total_name[0]




if __name__=="__main__":
#    from selenium.webdriver.chrome.service import Service as ChromeService
#    from selenium import webdriver
#    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
#    options = webdriver.ChromeOptions()
#    service = ChromeService(executable_path=path)
#    driver = webdriver.Chrome(service=service, options=options)

#    login(driver, "testled007@hotmail.com", "Aa123456")
#    assert_price_Maintain(driver, "VOLUME5A/S030UNVD835/22U/WH")
#    assert_price_Maintain_by_API("VOLUME5A/S030UNVD835/22U/WH","70.00")
      get_reportSaveSuccess_by_API()
