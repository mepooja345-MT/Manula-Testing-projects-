from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By

class PlacementsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'new_placement_drive_path'    :   (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[3]/div[2]/a'),
        'go_back_to_home_5_path'      : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[2]/div/a')
    }

    def new_placement_mt(self):
        self.new_placement_drive_path.click()

    def go_to_home_5_mt(self):
        self.go_back_to_home_5_path.click()