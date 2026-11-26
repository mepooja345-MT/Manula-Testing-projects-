
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class InterviewSchedules(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'Interview_schedule_path' : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[3]/div[3]/a') ,
        'go_back_to_home_7_path'  :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/fieldset/div[4]/a')
    }

    def interiew_schedule_mt(self):
        self.Interview_schedule_path.click()

    def go_to_home_7_mt(self):
        self.go_back_to_home_7_path.click()
