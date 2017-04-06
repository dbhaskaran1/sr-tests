import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest
import ConfigParser
import os

from Pages import LoginPage

class TestLoginPage(unittest.TestCase):

    config_file = ConfigParser.ConfigParser()
    config_file.read('frontend.conf')
    browser = os.environ['BROWSER']

    def get_browser(self):
        if self.browser == 'Chrome':
            return webdriver.Chrome()
        elif self.browser == 'Firefox':
            return webdriver.Firefox()
        else:
            exit -1

    def setup(self):
        print 'setup'

    def test_incorrect_pass(self):
        self.browser = self.get_browser()
        loginPage = LoginPage(self.browser)
        loginPage.navigate()
        loginPage.set_username('test@test.com')
        loginPage.set_password('password')
        loginPage.click_login()
        assert loginPage.login_error_message_shown()

    def test_correct_pass(self):
        self.browser = self.get_browser()
        loginPage = LoginPage(self.browser)
        loginPage.navigate()
        loginPage.set_username(self.config_file.get('creds','username'))
        loginPage.set_password(self.config_file.get('creds','password'))
        homePage = loginPage.click_login()
        assert homePage.check_dashboard_link_shows_up()

    def test_correct_pass1(self):
        self.browser = self.get_browser()
        loginPage = LoginPage(self.browser)
        loginPage.navigate()
        loginPage.set_username(self.config_file.get('creds1','username'))
        loginPage.set_password(self.config_file.get('creds1','password'))
        homePage = loginPage.click_login()
        assert homePage.check_dashboard_link_shows_up()

    def test_correct_pass2(self):
        self.browser = self.get_browser()
        loginPage = LoginPage(self.browser)
        loginPage.navigate()
        loginPage.set_username(self.config_file.get('creds2','username'))
        loginPage.set_password(self.config_file.get('creds2','password'))
        homePage = loginPage.click_login()
        assert homePage.check_dashboard_link_shows_up()

    def teardown(self):
        self.wd.quit()
