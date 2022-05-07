import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class reportPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.createProject_items=self.parse_config_file.getItemsFromSection(
            "report")
#        print(self.priceMantain_items)

    def saveReport_button(self):
        locateType, locateExpression = self.createProject_items['createproject.savereport'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)