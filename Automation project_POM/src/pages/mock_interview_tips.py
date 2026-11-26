from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class MockInterviewTips(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
      'interview_tips_path'          :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[5]/div[4]/a'),
      'go_back_to_home_11_path'      :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[4]/a')
               }

    def mock_tips_mt(self):
        self.interview_tips_path.click()

    def go_to_home_11_mt(self):
        self.go_back_to_home_11_path.click()