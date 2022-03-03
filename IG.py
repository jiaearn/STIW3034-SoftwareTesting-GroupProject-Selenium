import time
import unittest

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SignUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # open Firefox
        self.driver.get("https://www.instagram.com/")  # redirect to Instagram

    # INS01.01
    def test_0101_sign_up_invalid_email(self):
        time.sleep(3)  # wait for 3 seconds

        self.driver.find_element_by_xpath(
            "//span[contains(text(), 'Sign up')]/..").click()  # click sign up button

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_name('emailOrPhone')  # locate blank space for entering user phone or email
        fullname = self.driver.find_element_by_name('fullName')  # locate blank space for entering user full name
        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering user username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering user password

        email.clear()  # clear the blank space for phone or email
        fullname.clear()  # clear the blank space for full name
        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        email.send_keys("xo0faker0ogmail.com")  # input the blank space with this email
        fullname.send_keys("Faker Unknown")  # input the blank space with this full name
        username.send_keys("faker_unknown_000")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        signup = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

        errorMessage = self.driver.find_element_by_id('ssfErrorAlert').text  # locate the error message
        assert "Enter a valid email address." in errorMessage  # verify the error message

        time.sleep(3)  # wait for 3 seconds

    # INS01.02
    def test_0102_sign_up_invalid_username(self):
        time.sleep(3)  # wait for 3 seconds

        self.driver.find_element_by_xpath("//span[contains(text(), 'Sign up')]/..").click()  # click sign up button

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_name('emailOrPhone')  # locate blank space for entering user phone or email
        fullname = self.driver.find_element_by_name('fullName')  # locate blank space for entering user full name
        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering user username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering user password

        email.clear()  # clear the blank space for phone or email
        fullname.clear()  # clear the blank space for full name
        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        email.send_keys("xo0faker0o@gmail.com")  # input the blank space with this email
        fullname.send_keys("Faker Unknown")  # input the blank space with this full name
        username.send_keys("faker_unknown_00#")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        signup = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

        errorMessage = self.driver.find_element_by_id('ssfErrorAlert').text  # locate the error message
        assert "Usernames can only use letters, numbers, underscores and periods." in errorMessage  # verify the error message

        time.sleep(3)  # wait for 3 seconds

    # INS01.03
    def test_0103_sign_up_invalid_length_password(self):
        time.sleep(3)  # wait for 3 seconds

        self.driver.find_element_by_xpath("//span[contains(text(), 'Sign up')]/..").click()  # click sign up button

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_name('emailOrPhone')  # locate blank space for entering user phone or email
        fullname = self.driver.find_element_by_name('fullName')  # locate blank space for entering user full name
        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering user username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering user password

        email.clear()  # clear the blank space for phone or email
        fullname.clear()  # clear the blank space for full name
        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        email.send_keys("xo0faker0@gmail.com")  # input the blank space with this email
        fullname.send_keys("Faker Unknown")  # input the blank space with this full name
        username.send_keys("faker_unknown_000")  # input the blank space with this username
        password.send_keys("F")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        signup = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

    # INS01.04
    def test_0104_sign_up_valid_information(self):
        time.sleep(3)  # wait for 3 seconds

        self.driver.find_element_by_xpath("//span[contains(text(), 'Sign up')]/..").click()  # click sign up button

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_name('emailOrPhone')  # locate blank space for entering user phone or email
        fullname = self.driver.find_element_by_name('fullName')  # locate blank space for entering user full name
        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering user username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering user password

        email.clear()  # clear the blank space for phone or email
        fullname.clear()  # clear the blank space for full name
        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        email.send_keys("xo0faker0@gmail.com")  # input the blank space with this email
        fullname.send_keys("Faker Unknown")  # input the blank space with this full name
        username.send_keys("oo_faker_unknown_oo")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        signup = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

    def tearDown(self):
        self.driver.close()  # close the browser


class Login(unittest.TestCase):
    def setUp(self):
        self.uname = "instawebtesting3"  # declare the username
        self.email = "insta.webtesting2@outlook.com"  # declare the email
        self.pword = "Insta_Web1234"  # declare the password as pword
        self.npword = "Insta_Web12345"  # declare the new password as npword
        self.driver = webdriver.Firefox()  # open Firefox
        self.driver.get("https://www.instagram.com/")  # redirect to Instagram
        self.driver.implicitly_wait(30)  # waits maximum 30 seconds for elements present

    # INS02.01
    def test_0201_login_username_wrong_password(self):
        time.sleep(3)  # wait for 3 seconds

        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering password

        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        username.send_keys("faker_unknown_00")  # input the blank space with this username
        password.send_keys("Faker_000")  # input the blank space with this password

        login = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

        errorMessage = self.driver.find_element_by_id('slfErrorAlert').text  # locate the error message
        assert "Sorry, your password was incorrect. Please double-check your password." in errorMessage  # verify the error message

        time.sleep(3)  # wait for 3 seconds

    # INS02.02
    def test_0202_login_email_wrong_password(self):
        time.sleep(3)  # wait for 3 seconds

        email = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering email
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering password

        email.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        email.send_keys(self.email)  # input the blank space with this email
        password.send_keys("Faker_000")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        login = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

        errorMessage = self.driver.find_element_by_id('slfErrorAlert').text  # locate the error message
        time.sleep(5)
        assert "Sorry, your password was incorrect. Please double-check your password." in errorMessage  # verify the error message

        # time.sleep(3)  # wait for 3 seconds

    # INS02.03
    def test_0203_login_with_username(self):
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys(self.uname)  # insert username
        elem[1].send_keys(self.pword)  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//span[text()='Search']")))  # if the search bar is found within 20 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS02.04
    def test_0204_login_with_email(self):
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys(self.email)  # insert email
        elem[1].send_keys(self.pword)  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//span[text()='Search']")))  # If the search bar is found within 20 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element

    def tearDown(self):
        self.driver.close()  # close the browser


class ForgetPassword(unittest.TestCase):
    def setUp(self):
        self.uname = "instawebtesting3"  # declare the username
        self.email = "insta.webtesting2@outlook.com"  # declare the email
        self.pword = "Insta_Web123"  # declare the password as pword
        self.npword = "Insta_Web1234"  # declare the new password as npword
        self.driver = webdriver.Firefox()  # open Firefox
        self.driver.get("https://www.instagram.com")  # redirect to Instagram
        self.driver.implicitly_wait(30)  # waits maximum 30 seconds for elements present

    # INS03.01
    def test_0301_forget_with_email(self):
        self.driver.find_element_by_xpath(
            '//a[contains(@href, "%s")]' % "/accounts/password/reset/").click()  # find and click forgot password hyperlink
        self.driver.implicitly_wait(30)  # wait up to 30 seconds to go to the forgot password page
        self.driver.find_element_by_name("cppEmailOrUsername").send_keys(self.email)  # find textfield and insert email
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Send Login Link')]").click()  # click 'Send Login Link' button
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h4[text()='Email Sent']"
                 )))  # if the 'Email Send' text is found within 60 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS03.02
    def test_0302_forget_with_username(self):
        self.driver.find_element_by_xpath(
            '//a[contains(@href, "%s")]' % "/accounts/password/reset/").click()  # find and click forgot password hyperlink
        self.driver.implicitly_wait(30)  # wait up to 30 seconds to go to the forgot password page
        self.driver.find_element_by_name("cppEmailOrUsername").send_keys(
            self.uname)  # find textfield and insert username
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Send Login Link')]").click()  # click 'Send Login Link' button
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//h4[text()='Email Sent']")))  # if the 'Email Send' text is found within 60 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS03.03
    def test_0303_forget_with_wrong_email(self):
        self.driver.find_element_by_xpath(
            '//a[contains(@href, "%s")]' % "/accounts/password/reset/").click()  # find and click forgot password hyperlink
        self.driver.implicitly_wait(30)  # wait up to 30 seconds to go to the forgot password page
        self.driver.find_element_by_name("cppEmailOrUsername").send_keys(
            "111abcd111@gmail.com")  # find textfield and insert wrong email
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Send Login Link')]").click()  # click 'Send Login Link' button
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//p[contains(text(),'No users found')]")))  # if the 'No users found' text is found within 60 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS03.04
    def test_0304_forget_with_wrong_username(self):
        self.driver.find_element_by_xpath(
            '//a[contains(@href, "%s")]' % "/accounts/password/reset/").click()  # find and click forgot password hyperlink
        self.driver.implicitly_wait(30)  # wait up to 30 seconds to go to the forgot password page
        self.driver.find_element_by_name("cppEmailOrUsername").send_keys(
            "123456")  # find textfield and insert wrong username
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Send Login Link')]").click()  # click 'Send Login Link' button
        element = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//p[contains(text(),'No users found')]")))  # if the 'No users found' text is found within 60 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    def tearDown(self):
        self.driver.close()  # close the browser


class EditProfile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # open Firefox
        self.driver.get("https://www.instagram.com/")  # redirect to Instagram

    # INS04.01
    def test_0401_edit_invalid_email(self):
        time.sleep(3)  # wait for 3 seconds

        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering password

        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        username.send_keys("faker_unknown_00")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        login = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(5)  # wait for 3 seconds

        self.driver.find_element_by_css_selector("span._2dbep.qNELH").click()  # locate a human like symbol and click it
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # locate setting and click it

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_id('pepEmail')  # locate the email
        email.clear()  # clear the space/delete the present email
        email.send_keys("xo0faker0oxgmail.com")  # input the blank space with this email

        time.sleep(5)  # wait for 5 seconds

        button = self.driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()  # locate the button and click it

        time.sleep(5)  # wait for 5 seconds

    # INS04.02
    def test_0402_edit_valid_username(self):
        time.sleep(3)  # wait for 3 seconds

        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering password

        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        username.send_keys("faker_unknown_00")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        login = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(5)  # wait for 5 seconds

        self.driver.find_element_by_css_selector("span._2dbep.qNELH").click()  # locate a human like symbol and click it
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # locate setting and click it

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_id("pepUsername")  # locate the email
        email.clear()  # clear the space/delete the present email
        email.send_keys("faker_unknown_01")  # input the blank space with this email

        time.sleep(5)  # wait for 5 seconds

        button = self.driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()  # locate the button and click it

        time.sleep(5)  # wait for 5 seconds

    # INS04.03
    def test_0403_edit_change_back_username(self):
        time.sleep(3)  # wait for 3 seconds

        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering password

        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        username.send_keys("faker_unknown_00")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        login = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(5)  # wait for 5 seconds

        self.driver.find_element_by_css_selector("span._2dbep.qNELH").click()  # locate a human like symbol and click it
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # locate setting and click it

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_id('pepUsername')  # locate the email
        email.clear()  # clear the space/delete the present email
        email.send_keys("faker_unknown_00")  # input the blank space with this email

        time.sleep(5)  # wait for 5 seconds

        button = self.driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()  # locate the button and click it

        time.sleep(5)  # wait for 5 seconds

    # INS04.04
    def test_0404_edit_valid_email(self):
        time.sleep(3)  # wait for 3 seconds

        username = self.driver.find_element_by_css_selector(
            "input[name='username']")  # locate blank space for entering username
        password = self.driver.find_element_by_css_selector(
            "input[name='password']")  # locate blank space for entering password

        username.clear()  # clear the blank space for username
        password.clear()  # clear the blank space for password

        username.send_keys("faker_unknown_00")  # input the blank space with this username
        password.send_keys("Faker_00")  # input the blank space with this password

        time.sleep(5)  # wait for 5 seconds

        login = self.driver.find_element_by_css_selector(
            "button[type='submit']").click()  # locate the button and click it

        time.sleep(3)  # wait for 3 seconds

        self.driver.find_element_by_css_selector("span._2dbep.qNELH").click()  # locate a human like symbol and click it
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # locate setting and click it

        time.sleep(5)  # wait for 5 seconds

        email = self.driver.find_element_by_id('pepEmail')  # locate the email
        email.clear()  # clear the space/delete the present email
        email.send_keys("x9810077@gmail.com")  # input the blank space with this email

        time.sleep(5)  # wait for 5 seconds

        button = self.driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()  # locate the button and click it

        time.sleep(5)  # wait for 5 seconds

    def tearDown(self):
        self.driver.close()  # close the browser


class ChangePassword(unittest.TestCase):
    def setUp(self):
        self.uname = "instawebtesting3"  # declare the username
        self.email = "insta.webtesting2@outlook.com"  # declare the email
        self.npword = "Insta_Web12345"  # declare the password as pword
        self.pword = "Insta_Web1234"  # declare the new password as npword
        self.driver = webdriver.Firefox()  # open Firefox
        self.driver.get("https://www.instagram.com")  # redirect to Instagram
        self.driver.implicitly_wait(30)  # waits maximum 30 seconds for elements present

    # INS05.01
    def test_0501_invalid_password_change_password(self):
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys(self.uname)  # insert username
        elem[1].send_keys(self.pword)  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button
        self.driver.find_element_by_css_selector(
            "span._2dbep.qNELH").click()  # click “Profile” button at the navigation bar
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # click “Setting” button
        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Change Password')]").click()  # click “Change Password” at side bar
        self.driver.find_element_by_id("cppOldPassword").send_keys(
            "Insta_Web1")  # insert wrong password in Old Password text field
        self.driver.find_element_by_id("cppNewPassword").send_keys(
            self.npword)  # insert new password in New Password text field
        self.driver.find_element_by_id("cppConfirmPassword").send_keys(
            self.npword)  # insert new password  in Confirm New Password text field
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Change Password')]").click()  # click “Change Password” button
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//p[contains(text(),'Your old password was entered incorrectly. Please enter it again.')]")))
        # if the text is found within 20 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS05.02
    def test_0502_invalid_format_change_password(self):
        time.sleep(5)
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys(self.uname)  # insert username
        elem[1].send_keys(self.pword)  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button
        self.driver.find_element_by_css_selector(
            "span._2dbep.qNELH").click()  # click “Profile” button at the navigation bar
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # click “Setting” button
        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Change Password')]").click()  # click “Change Password” at side bar
        self.driver.find_element_by_id("cppOldPassword").send_keys(
            self.pword)  # insert old password in Old Password text field
        self.driver.find_element_by_id("cppNewPassword").send_keys(
            "123")  # insert wrong format password in New Password text field
        self.driver.find_element_by_id("cppConfirmPassword").send_keys(
            "123")  # insert wrong format password in Confirm New Password text field
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Change Password')]").click()  # click “Change Password” button
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(),'This password is too easy to guess. Please create a new one.')]")))
        # if the text is found within 20 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS05.03
    def test_0503_unmatch_change_password(self):
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys(self.uname)  # insert username
        elem[1].send_keys(self.pword)  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button
        self.driver.find_element_by_css_selector(
            "span._2dbep.qNELH").click()  # click “Profile” button at the navigation bar
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # click “Setting” button
        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Change Password')]").click()  # click “Change Password” at side bar
        self.driver.find_element_by_id("cppOldPassword").send_keys(
            self.pword)  # insert old password in Old Password text field
        self.driver.find_element_by_id("cppNewPassword").send_keys(
            "123456123")  # insert new password in New Password text field
        self.driver.find_element_by_id("cppConfirmPassword").send_keys(
            "123456abc")  # insert unmatch new password in New Password text field
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Change Password')]").click()  # click “Change Password” button
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[contains(text(),'Please make sure both passwords match.')]")))
        # if the text is found within 20 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    # INS05.04
    def test_0504_change_password(self):
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys("instawebtesting")  # insert username
        elem[1].send_keys("Insta_Web123")  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button
        self.driver.find_element_by_css_selector(
            "span._2dbep.qNELH").click()  # click “Profile” button at the navigation bar
        self.driver.find_element_by_xpath(
            "//div[contains(text(), 'Settings')]/../../../../../..").click()  # click “Setting” button
        self.driver.find_element_by_xpath(
            "//a[contains(text(), 'Change Password')]").click()  # click “Change Password” at side bar
        self.driver.find_element_by_id("cppOldPassword").send_keys(
            "Insta_Web123")  # insert old password in Old Password text field
        self.driver.find_element_by_id("cppNewPassword").send_keys(
            "Insta_Web12345")  # insert new password in New Password text field
        self.driver.find_element_by_id("cppConfirmPassword").send_keys(
            "Insta_Web12345")  # insert confirm new password in New Password text field
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Change Password')]").click()  # click “Change Password” button
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.XPATH, "//p[contains(text(),'Password changed.')]")))
        # if the text is found within 20 seconds, set the element to true, otherwise false
        time.sleep(5)
        assert element  # verify the element

    def tearDown(self):
        self.driver.close()  # close the browser


class CreatePost(unittest.TestCase):
    def setUp(self):
        self.uname = "faker_unknown_00"  # declare the username
        self.pword = "Faker_00"  # declare the password as pword
        self.filepath = "C:\\Users\\ASUS\\Desktop\\SoftwareTesting\\"  # declare the filepath

        self.driver = webdriver.Firefox()  # open Firefox
        self.driver.get("https://www.instagram.com")  # redirect to Instagram
        self.driver.implicitly_wait(30)  # waits maximum 30 seconds for elements present
        elem = self.driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")  # find input text field
        elem[0].send_keys(self.uname)  # insert username
        elem[1].send_keys(self.pword)  # insert password
        self.driver.find_element_by_xpath("//div[contains(text(), 'Log In')]/..").click()  # click login button

    # INS06.01
    def test_0601_post_image(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector(
            "button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        # elem.send_keys(Keys.RETURN)
        pyautogui.write("{0}testimg0.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.02
    def test_0602_post_video(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testvid.mp4".format(self.filepath))  # select video from local file
        pyautogui.press("enter")  # press enter button
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.03
    def test_0603_post_multiple(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button.
        pyautogui.write("{0}testimg1.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        time.sleep(5)  # wait for 5 second
        driver.find_elements_by_css_selector("button.sqdOP.yWX7d.y3zKF")[4].click()  # click multiple image button
        driver.find_element_by_css_selector("div.z-nxm").click()  # click "Plus" button
        pyautogui.write("{0}testimg2.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        time.sleep(5)  # wait for 5 second
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.04
    def test_0604_post_landscape(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testlandscape.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        time.sleep(5)  # wait for 5 second
        driver.find_elements_by_css_selector("div.RJJyf._1gKD_ > button.sqdOP.yWX7d.y3zKF")[
            0].click()  # click edit size button
        driver.find_elements_by_css_selector("div.YAPUk.gdFG_ > button.sqdOP.yWX7d.y3zKF")[
            3].click()  # click “16:9” button.
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.05
    def test_0605_post_portrait(self):
        driver = self.driver
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button.
        pyautogui.write("{0}testportrait.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        time.sleep(5)  # wait for 5 second
        driver.find_elements_by_css_selector("div.RJJyf._1gKD_ > button.sqdOP.yWX7d.y3zKF")[
            0].click()  # click edit size button
        driver.find_elements_by_css_selector("div.YAPUk.gdFG_ > button.sqdOP.yWX7d.y3zKF")[
            2].click()  # click “4:5” button.
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.06
    def test_0606_discard_post(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testimg2.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        time.sleep(5)  # wait for 5 second
        driver.find_element_by_xpath(
            "//div[contains(@class, 'RnEpo gpWnf Yx5HN')]/div/button").click()  # click “X” button
        time.sleep(2.5)  # wait for 2.5 second
        driver.find_element_by_xpath("//button[contains(text(), 'Discard')]").click()  # click the “Discard” button
        time.sleep(5)
        assert "/create/" not in driver.current_url  # check if the "/create/" not exists in url

    # INS06.07
    def test_0607_apply_filter(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testimg3.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath("//div[contains(text(), 'Clarendon')]/..").click()  # click “Clarendon” filter
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.08
    def test_0608_add_caption(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testimg4.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_css_selector("textarea.lFzco").send_keys(
            "Test caption")  # find textfield and insert "Test caption"
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.09
    def test_0609_add_hashtag(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testimg5.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_css_selector("textarea.lFzco").send_keys("#test")  # find textfield and insert a hashtag
        time.sleep(5)  # wait for 5 second
        driver.find_elements_by_css_selector("button.Eo_F0")[0].click()  # click first result on the hashtag list
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    # INS06.10
    def test_0610_tag_account(self):
        driver = self.driver  # log in to account
        driver.find_element_by_css_selector("button.wpO6b.ZQScA").click()  # click “Plus” button at the navigation bar
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Select from computer')]").click()  # click “Select from Computer” button
        pyautogui.write("{0}testimg6.jpg".format(self.filepath))  # select image from local file
        pyautogui.press("enter")  # press enter button

        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the crop image function
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Next')]").click()  # click next button to skip the edit image function
        driver.find_element_by_css_selector("div.civB6").click()  # press on the image
        driver.find_element_by_css_selector("input.j_2Hd.iwQA6.RO68f.M5V28").send_keys(
            self.uname)  # type the current Instagram name in the textbox.
        driver.find_elements_by_css_selector("button.osCPk")[0].click()  # click first result on the list.
        driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()  # click share button
        time.sleep(5)
        status = driver.find_element_by_css_selector(
            "h2._7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv.l4b0S").text  # locate the successful message as status
        time.sleep(3)
        assert "Your post has been shared." in status  # check if the text exists in "status"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    test_classes_to_run = [SignUp, Login, EditProfile, ForgetPassword, ChangePassword, CreatePost]  # create an array
    # to hold all test classes

    loader = unittest.TestLoader()  # call a method to search for test cases

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)  # use loader to search for test cases
        suites_list.append(suite)  # construct a test set

    big_suite = unittest.TestSuite(suites_list)  # used to aggregate tests that should be executed together

    runner = unittest.TextTestRunner()  # call a method to execute the test set
    results = runner.run(big_suite)  # execute the test set
