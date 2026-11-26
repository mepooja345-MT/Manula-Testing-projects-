from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class SelfIntroduction(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
      'self_intro_path'         : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[6]/div[2]/a'),
      'go_back_to_home_9_path'  : (By.XPATH , '/html/body/form/div[3]/div/div/div/div/div/div/div/div/b/div[2]/a')
               }

    def self_intro_mt(self):
        self.self_intro_path.click()

    def go_to_home_9_mt(self):
        self.go_back_to_home_9_path.click()