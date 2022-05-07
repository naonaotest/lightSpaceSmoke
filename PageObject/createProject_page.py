import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class CreateProjectPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.createProject_items=self.parse_config_file.getItemsFromSection(
            "createProject")
#        print(self.priceMantain_items)

    def createprojectblock(self):
        locateType, locateExpression = self.createProject_items['createproject.createprojectblock'].split(">")
#        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def rectangle_button(self):
        locateType, locateExpression = self.createProject_items['createproject.rectangle_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def irregular_button(self):
        locateType, locateExpression = self.createProject_items['createproject.irregular_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def subzone_button(self):
        locateType, locateExpression = self.createProject_items['createproject.subzone_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def zoneSettings_button(self):
        locateType, locateExpression = self.createProject_items['createproject.zonsettings_Function_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def openWorkspace_button(self):
        locateType, locateExpression = self.createProject_items['createproject.openworkspace_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def intelligentDesign_button(self):
        locateType, locateExpression = self.createProject_items['createproject.intelligentdesign_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def afterIntelligentSave_button(self):
        locateType, locateExpression = self.createProject_items['createproject.save_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def projectName_button(self):
        locateType, locateExpression = self.createProject_items['createproject.projectname_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def viewFullReport_button(self):
        locateType, locateExpression = self.createProject_items['createproject.viewfullreport_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def bestprice_button(self):
        locateType, locateExpression = self.createProject_items['createproject.bestprice_button'].split(">")
        #        print(locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)


#    def light_productname_button(self):
#        locateType, locateExpression = self.createProject_items['createproject.light_productname_button'].split(">")
#        print(locateType, locateExpression)
#        return find_element(self.driver, locateType, locateExpression)

#    def light_price_text(self):
#        locateType, locateExpression = self.createProject_items['createproject.ligth_productprce_text'].split(">")
        #        print(locateType, locateExpression)
#        return find_element(self.driver, locateType, locateExpression)



