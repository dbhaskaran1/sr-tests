import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest

from Pages import LoginPage

class TestLoginPage(unittest.TestCase):

    def setup(self):
        print 'setup'

    def test_incorrect_pass(self):
        self.browser = webdriver.Chrome()
        loginPage = LoginPage(self.browser)
        loginPage.navigate()
        loginPage.set_username('test@test.com')
        loginPage.set_password('password')
        loginPage.click_login()
        assert loginPage.login_error_message_shown()

    def test_correct_pass(self):
        self.browser = webdriver.Chrome()
        loginPage = LoginPage(self.browser)
        loginPage.navigate()
        loginPage.set_username('test1@smartresponse.org')
        loginPage.set_password('test#1')
        loginPage.click_login()

    def incorrect_password(self):
        wd = self.wd
        login_button = wd.find_element_by_id('login_button')
        email_field = wd.find_element_by_id('email')
        password_field = wd.find_element_by_id('password')

        email_field.send_keys('test@test.com')
        password_field.send_keys('password')

        login_button.click()
        time.sleep(1)
        error_message = wd.find_element_by_xpath('//div[ contains(text(),"Incorrect login information") ]')
        assert error_message.text == 'Incorrect login information'

    def teardown(self):
        self.wd.quit()
