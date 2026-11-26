from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class CourseMaterials(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'course_material_path'   : (By.XPATH,   '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[4]/div[1]/a')
    }

    def course_material_mt(self):
        self.course_material_path.click()


