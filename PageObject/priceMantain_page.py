#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class PriceMantainPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.priceMantain_items=self.parse_config_file.getItemsFromSection(
            "priceMantain")
#        print(self.priceMantain_items)

    def priceMaintainBlock(self):
        locateType, locateExpression = self.priceMantain_items['pricemaintain_page.pricemaintainblock'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def priceMaintainEditButton(self):
        locateType,locateExpression=self.priceMantain_items['pricemaintain_page.editbutton'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType,locateExpression)

    def priceMaintainChange1Box(self):
        locateType,locateExpression=self.priceMantain_items['pricemaintain_page.changeprice1'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType,locateExpression)

    def priceMaintainChange2Box(self):
        locateType,locateExpression=self.priceMantain_items['pricemaintain_page.changeprice2'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType,locateExpression)

    def priceMaintainConfirmButton(self):
        locateType,locateExpression=self.priceMantain_items['pricemaintain_page.confirm'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType,locateExpression)

if __name__=="__main__":
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium import webdriver
    path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    service = ChromeService(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    aa=PriceMantainPage(driver)
    aa.priceMaintainBlock()
    aa.priceMaintainChange1Box()
    aa.priceMaintainChange2Box()
    aa.priceMaintainConfirmButton()
