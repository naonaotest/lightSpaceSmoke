#encoding=utf-8
from configparser import ConfigParser
from ProjectVar.var import page_object_repository_path

class ParsePageObjectRepositoryConfig(object):
    def __init__(self):
        self.cf=ConfigParser()
        self.cf.read(page_object_repository_path,encoding="utf-8")

    def getItemsFromSection(self,sectionName):
        return dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__=="__main__":
    pp=ParsePageObjectRepositoryConfig()
    print(pp.getItemsFromSection("LightSpace_login"))
    print(pp.getOptionValue("LightSpace_login","login_page.username"))


