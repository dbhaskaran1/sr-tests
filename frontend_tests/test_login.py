import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest

from Pages import LoginPage

class TestLoginPage(unittest.TestCase):

    def setup(self):
        print 'setup'

    #@pytest.mark.skip
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
        homePage = loginPage.click_login()
        assert homePage.check_dashboard_link_shows_up()


    def teardown(self):
        self.wd.quit()
