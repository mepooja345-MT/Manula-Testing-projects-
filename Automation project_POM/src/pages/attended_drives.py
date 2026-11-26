from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class AttendedDrives(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
      'attended_drives_path' : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[3]/div[5]/a'),
      'go_back_to_home_8_path'  : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[4]/a')
               }

    def attended_drives_mt(self):
        self.attended_drives_path.click()

    def go_to_home_8_mt(self):
        self.go_back_to_home_8_path.click()