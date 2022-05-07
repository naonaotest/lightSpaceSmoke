#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class MyReport_Page(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.priceMantain_items=self.parse_config_file.getItemsFromSection(
            "myReport")
        print(self.priceMantain_items)

    def my_report_Block(self):
        locateType, locateExpression = self.priceMantain_items['myreport_page.myreportblock'].split(">")
        print('myreport_page.myreportblock',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def my_report_deleteConfirm_Button(self):
        locateType, locateExpression = self.priceMantain_items['myreport_page.deleteconfirmbutton'].split(">")
        print('myreport_page.myreportblock',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)