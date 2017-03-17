import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class BasePage(object):
    url = ''

    def __init__(self, driver):
        self.wd = driver

    def navigate(self):
        self.wd.get(self.url)

class LoginPage(BasePage):
    url = 'https://dev.smartresponse.org/' + '/login'
    login_identifier = (By.ID, 'login_button')
    email_identifier = (By.ID, 'email')
    password_identifier = (By.ID, 'password')

    def set_password(self, password):
        elem = self.wd.find_element(*LoginPage.password_identifier)
        elem.clear()
        elem.send_keys(password)

    def set_username(self, username):
        elem = self.wd.find_element(*LoginPage.email_identifier)
        elem.clear()
        elem.send_keys(username)

    def click_login(self):
        elem = self.wd.find_element(*LoginPage.login_identifier)
        elem.click()

    def login_error_message_shown(self):
        time.sleep(1)
        error_message = self.wd.find_element_by_xpath('//div[ contains(text(),"Incorrect login information") ]')
        return error_message.text == 'Incorrect login information'
