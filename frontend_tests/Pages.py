import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ConfigParser

class BasePage(object):
    url = ''

    def __init__(self, driver):
        self.wd = driver

    def navigate(self):
        self.wd.get(self.url)

    def wait_for_item_to_load(self, id_scheme, id_value, timeout=30):
        elem = WebDriverWait(self.wd, timeout=timeout).until(
            EC.presence_of_element_located((id_scheme, id_value))
        )
        if elem:
            return True
        else:
            return False


class LoginPage(BasePage):
    url = 'https://dev.smartresponse.org' + '/login'
    login_identifier = (By.ID, 'login_button')
    email_identifier = (By.ID, 'email')
    password_identifier = (By.ID, 'password')
    error_message_identifier = (By.XPATH, '//div[ contains(text(),"Incorrect login information") ]')

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
        return AdminDashboard(self.wd)

    def login_error_message_shown(self):
        time.sleep(1)
        print self.error_message_identifier
        if self.wait_for_item_to_load(id_scheme=self.error_message_identifier[0],
                                      id_value=self.error_message_identifier[1]):
            return True
        else:
            return False

class AdminDashboard(BasePage):
    url = 'https://dev.smartresponse.org' + '/dashboard'
    dashboard_identifier = (By.PARTIAL_LINK_TEXT, 'Dashboard')

    def check_on_right_page(self):
        print self.wd.current_url
        assert self.wd.current_url == self.url

    def check_dashboard_link_shows_up(self):
        if self.wait_for_item_to_load(id_scheme=self.dashboard_identifier[0],
                                          id_value=self.dashboard_identifier[1]):
            return True
        else:
            return False

