from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class QrCode(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'QR_code_path'   : (By.XPATH,  '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[6]/div[4]/a')
    }

    def QR_code_mt(self):
        self.QR_code_path.click()