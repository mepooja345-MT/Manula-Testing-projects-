from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class ModelResume(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
      'model_resume_path'          :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[4]/div[2]/a'),
      'go_back_to_home_10_path'    :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/div[4]/a')
               }

    def model_resume_mt(self):
        self.model_resume_path.click()

    def go_to_home_10_mt(self):
        self.go_back_to_home_10_path.click()

