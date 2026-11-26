
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class AppliedDrives(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
                  'Applied_drives_path'         :   (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[3]/div[4]/a'),
                  'go_back_to_home_6_path'      :   (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/fieldset/div[2]/a')
               }
    def applied_drives_mt(self):
        self.Applied_drives_path.click()

    def go_to_home_6(self):
        self.go_back_to_home_6_path.click()

