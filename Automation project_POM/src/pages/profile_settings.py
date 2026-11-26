
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By

class ProfileSettings(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'profile_settings_path'         :  (By.XPATH, '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div[4]/div[3]/a'),
        'contact_details_path'          :  (By.XPATH, '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div[7]/div[2]/div/a'),
        'whatsapp_button_path'          :  (By.XPATH, '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div[3]/div[2]/div/table/tbody/tr/td[1]/input'),
        'saving_con_details_path'       :  (By.XPATH,'/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div[3]/div[5]/div[4]/input'),
        'go_back_to_home_1_path'        :  (By.XPATH, '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div[3]/div[5]/div[2]/a'),
        'education_details_path'        :  (By.XPATH, '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div[7]/div[3]/div/a'),
        'go_back_to_home_2_path'        :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[2]/button/a'),
        'update_resume_path'            :  (By.XPATH, '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div[7]/div[4]/div/a'),
        'browse_resume_path'            :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/fieldset[1]/div[1]/div[2]/input'),
        'upload_resume_path'            :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/fieldset[1]/div[1]/div[3]/input[2]'),
        'go_back_to_home_3_path'        :  (By.XPATH , '/html/body/form/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/a')

    }

# mt - method

    def profile_settings_mt(self):
        self.profile_settings_path.click()
                                     # here we are not writing change password feature cause there won't  be any change in url
    def contact_details_mt(self):
        self.contact_details_path.click()
    #
    def whatsapp_mt(self):
        self.whatsapp_button_path.click()

    def saving_con_det_mt(self):
        self.saving_con_details_path.click()

    def go_to_home_1_mt(self):
        self.go_back_to_home_1_path.click()

    def edu_det_mt(self):
        self.education_details_path.click()

    def go_to_home_2_mt(self):
        self.go_back_to_home_2_path.click()

    def resume_upload_mt(self):
        self.update_resume_path.click()

    def browse_resume_mt(self):
        self.browse_resume_path.click()

    def update_resume_mt(self):
        self.upload_resume_path.click()

    def go_to_home_3_mt(self):
        self.go_back_to_home_3_path.click()

