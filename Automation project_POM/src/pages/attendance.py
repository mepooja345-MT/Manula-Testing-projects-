from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class Attendance(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'attendance_path'   : (By.XPATH,   '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[7]/div[1]/a')
    }

    def attendance_mt(self):
        self.attendance_path.click()