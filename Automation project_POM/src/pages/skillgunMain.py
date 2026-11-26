from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
class SkillGunMain(PageFactory):
     def __init__(self, driver):
           self.driver = driver


     locators = { 'mobile'   :  ( By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/input'),     # mobile
                 'email'     : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[1]/input ') ,    # email
                 'password'  : (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[2]/input' ),  # password
                  'cb'       : (By.XPATH ,  '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[4]/input '), # checkbox
                  'lg'       :( By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[9]/input')   # login button
     }



     def mobile_num(self , mobile):
         self.mobile.send_keys('7842364872')    # remember  self you are forgetting

     def email_id(self , email):
         self.email.send_keys("pooja09020112@gmail.com")

     def pw(self ,password ):
         self.password.send_keys("poojatechpwd")

     def checkbox(self):
         self.cb.click()

     def login(self):
         self.lg.click()

