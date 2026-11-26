from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class ReferFriend(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'refer_friend_path'   : (By.XPATH,  '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[3]/div[1]/a')
    }

    def refer_friend_mt(self):
        self.refer_friend_path.click()