#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig

class myProjectPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.myProject_items=self.parse_config_file.getItemsFromSection(
            "myProject")
#        print(self.myProject_items)



    def myProjectBlock(self):
        locateType, locateExpression = self.myProject_items['myproject_page.myprojectblock'].split(">")
#        print('myproject_page.myprojectblock',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def ongoingprojectsbutton(self):
        locateType, locateExpression = self.myProject_items['myproject_page.ongoingprojectsbutton'].split(">")
#        print('myproject_page.ongoingprojectsbutton',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def completedprojectsbutton(self):
        locateType, locateExpression = self.myProject_items['myproject_page.completedprojectsbutton'].split(">")
#        print('myproject_page.completedprojectsbutton',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def ongoingproject_edit1button(self):
        locateType, locateExpression = self.myProject_items['myproject_page.ongoingproject_edit1button'].split(">")
#        print('myproject_page.ongoingproject_edit1button',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)

    def ongoingproject_delete1button(self):
        locateType, locateExpression = self.myProject_items['myproject_page.ongoingproject_delete1button'].split(">")
#        print('myproject_page.ongoingproject_delete1button',locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)


    def ongoing_delete_confirmbutton(self):
        locateType, locateExpression = self.myProject_items['myproject_page.ongoing_delete_confirmbutton'].split(">")
#        print('myproject_page.ongoing_delete_confirmbutton', locateType, locateExpression)
        return find_element(self.driver, locateType, locateExpression)



if __name__=="__main__":
    pass





