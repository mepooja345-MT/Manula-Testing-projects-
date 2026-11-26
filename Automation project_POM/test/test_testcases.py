from selenium import webdriver
import time
from src.pages.skillgunMain import SkillGunMain
from src.pages.placements import PlacementsPage
from src.pages.profile_settings import ProfileSettings
from src.pages.AppliedDrives import AppliedDrives
from src.pages.Interview import InterviewSchedules
from src.pages.attended_drives import AttendedDrives
from src.pages.course_materials import CourseMaterials
from src.pages.attendance import Attendance
from src.pages.QR_code import QrCode
from src.pages.self_intoduction import SelfIntroduction
from src.pages.Refer_friend import ReferFriend
from src.pages.model_resume import ModelResume
from src.pages.mock_interview_tips import MockInterviewTips
driver = webdriver.Chrome()

def test_skillgun_main_tc():
    driver.get("http://skillgun.com")

    s = SkillGunMain(driver)
    time.sleep(2)
    s.mobile_num('78******72')
    time.sleep(2)
    s.email_id('pooja********@gmail.com')
    time.sleep(1)
    s.pw('pooja*******')
    time.sleep(3)
    s.checkbox()
    time.sleep(7)  # enter captcha manually
    s.login()
    assert 'Home' in driver.current_url                            # testcase_1

def test_profile_settings_tc():
    a1 = ProfileSettings(driver)
    a1.profile_settings_mt()
    time.sleep(2)
    assert 'ProfileSetting' in driver.current_url                   # testcase_2

def test_edit_contact_details_tc():
    a2 = ProfileSettings(driver)
    a2.contact_details_mt()
    time.sleep(3)
    assert 'EditContactDetails' in driver.current_url              ## testcase_3
    a2.whatsapp_mt()
    time.sleep(2)
    a2.saving_con_det_mt()
    time.sleep(2)
    a2.go_to_home_1_mt()
    time.sleep(3)
    a2.profile_settings_mt()
    time.sleep(2)

def test_edit_education_details_tc():
    a3 = ProfileSettings(driver)
    a3.edu_det_mt()
    time.sleep(2)
    assert 'EducationDetails' in driver.current_url                   # # testcase_4
    a3.go_to_home_2_mt()
    time.sleep(3)
    a3.profile_settings_mt()
    time.sleep(3)

def test_update_resume_tc():
    a4 = ProfileSettings(driver)
    a4.resume_upload_mt()
    time.sleep(3)
    a4.browse_resume_mt()
    time.sleep(10)
    a4.update_resume_mt()
    time.sleep(2)
    assert 'UploadResume' in driver.current_url                         # # testcase_5
    time.sleep(3)
    a4.go_to_home_3_mt()
    time.sleep(3)

def test_placements_apply_tc():
    a5 = PlacementsPage(driver)
    a5.new_placement_mt()
    time.sleep(3)
    assert 'NewPlacementDrive' in driver.current_url                      # testcase_6
    time.sleep(3)
    a5.go_to_home_5_mt()
    time.sleep(3)

def test_applied_drives_tc():
    a6 = AppliedDrives(driver)
    a6.applied_drives_mt()
    time.sleep(3)
    assert 'AppliedDrives' in driver.current_url                           # testcase_7
    time.sleep(3)
    a6.go_to_home_6()
    time.sleep(3)

def test_interview_schedule_tc():
        a7 = InterviewSchedules(driver)
        a7.interiew_schedule_mt()
        time.sleep(3)
        assert 'Interviews' in driver.current_url                          # testcase_8
        time.sleep(3)
        a7.go_to_home_7_mt()
        time.sleep(3)

def test_attended_drives_tc():
    a8 = AttendedDrives(driver)
    a8.attended_drives_mt()
    time.sleep(3)
    assert 'AttendedDriveDetails' in driver.current_url                      # testcase_9
    time.sleep(3)
    a8.go_to_home_8_mt()
    time.sleep(3)


def test_course_materials_tc():
    a9 = CourseMaterials(driver)
    a9.course_material_mt()
    time.sleep(3)
    assert 'CourseMaterial' in driver.current_url                             #testcase_10
    time.sleep(3)
    driver.back()
    time.sleep(3)

def test_attendance_tc():
    a10 = Attendance(driver)
    a10.attendance_mt()
    time.sleep(3)
    assert 'DisplayStudentAttendance' in driver.current_url                   # testcase_11
    time.sleep(3)
    driver.back()
    time.sleep(3)

def test_Qrcode_tc():
    a11 = QrCode(driver)
    a11.QR_code_mt()
    time.sleep(3)
    assert 'Student_QR_Code' in driver.current_url                            #testcase_12
    time.sleep(3)
    driver.back()
    time.sleep(3)

def test_self_intro_tc():
    a12 = SelfIntroduction(driver)
    a12.self_intro_mt()
    time.sleep(3)
    assert 'SelfIntroduction' in driver.current_url                         #testcase_13
    time.sleep(3)
    a12.go_to_home_9_mt()
    time.sleep(3)

def test_refer_friend_tc():
    a13 = ReferFriend(driver)
    a13.refer_friend_mt()
    time.sleep(3)
    assert 'AddReference' in driver.current_url                            #testcase_14
    time.sleep(3)
    driver.back()
    time.sleep(3)

def test_model_resume_tc():
    a13 = ModelResume(driver)
    a13.model_resume_mt()
    time.sleep(3)
    assert 'ModelResumes' in driver.current_url                         #testcase_15
    time.sleep(3)
    a13.go_to_home_10_mt()
    time.sleep(3)

def test_mock_tips_tc():
    a14 = MockInterviewTips(driver)
    a14.mock_tips_mt()
    time.sleep(3)
    assert 'MockInterviewTips' in driver.current_url                         #testcase_16
    time.sleep(3)
    a14.go_to_home_11_mt()
    time.sleep(3)

