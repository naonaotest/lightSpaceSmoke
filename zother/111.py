import time

import pyautogui
from ProjectVar.var import *

time.sleep(3)
print(pyautogui.position())
#Point(x=1318, y=481)
#Point(x=330, y=500)
#Point(x=385, y=499)
#Point(x=26, y=514)

#Report page----edit
#Point(x=85, y=613)


from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

#path = project_path + '\\webdriver\\chromedriver_win32\\chromedriver.exe'
#options = webdriver.ChromeOptions()
#service = ChromeService(executable_path=path)
#driver = webdriver.Chrome(service=service, options=options)
#print(driver.get_window_size())
#print(driver.get_window_position())
#driver.maximize_window()
#print(driver.get_window_size())
#print(driver.get_window_position())

#{'width': 1050, 'height': 708}
#{'x': 10, 'y': 10}
#{'width': 1382, 'height': 744}
#{'x': -8, 'y': -8}
