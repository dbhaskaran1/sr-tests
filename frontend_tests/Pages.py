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

    def check_on_right_page(self):
        assert self.wd.current_url == self.url

class LoginPage(BasePage):
    config = ConfigParser.ConfigParser()
    config.read('frontend.conf')
    url = config.get('site','login_page')

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
        if self.wait_for_item_to_load(id_scheme=self.error_message_identifier[0],
                                      id_value=self.error_message_identifier[1]):
            return True
        else:
            return False

class AdminDashboard(BasePage):
    url = 'https://dev.smartresponse.org' + '/dashboard'
    dashboard_identifier = (By.PARTIAL_LINK_TEXT, 'Dashboard')


    def check_dashboard_link_shows_up(self):
        if self.wait_for_item_to_load(id_scheme=self.dashboard_identifier[0],
                                          id_value=self.dashboard_identifier[1]):
            return True
        else:
            return False


class DashboardOrganizations(BasePage):
    url = 'https://dev.smartresponse.org' + '/dashboard' + '/organization'
    add_org_identifier = (By.PARTIAL_LINK_TEXT, 'Add Organization')
    export_identifier = (By.PARTIAL_LINK_TEXT, 'Export')
    print_identifier = (By.PARTIAL_LINK_TEXT, 'Print')



class RegistrationPage(BasePage):
    url = 'https://dev.smartresponse.org' + '/registration'
    org_name_identifier = (By.ID, 'org_name')
    first_name_identifier = (By.ID, 'first_name')
    last_name_identifier = (By.ID, 'last_name')
    phone_number_identifier = (By.ID, 'phoneNumber')
    email_identifier = (By.ID, 'email')
    password_identifier = (By.ID, 'password')
    password_confirm_identifier = (By.ID, 'passwordConfirmation')
    auth_identifier = (By.ID, 'auth_checkbox')
    recaptcha_identifier = (By.XPATH, '//div[contains(@class, "recaptcha-checkbox-checkmark")]')
    add_organization_identifier = (By.XPATH, "//button[contains(text(),'Add Organization')]")

    def click_add_organization(self):
        elem = self.wd.find_element(*RegistrationPage.add_organization_identifier)
        elem.click()
        return AdminDashboard(self.wd)

    def set_names(self, first_name, last_name):
        elem = self.wd.find_element(*RegistrationPage.first_name_identifier)
        elem.clear()
        elem.send_keys(first_name)
        elem = self.wd.find_element(*RegistrationPage.last_name_identifier)
        elem.clear()
        elem.send_keys(last_name)

    def set_phone_number(self, phone_number):
        elem = self.wd.find_element(*RegistrationPage.phone_number_identifier)
        elem.clear()
        elem.send_keys(phone_number)

    def set_mail(self, email_id):
        elem = self.wd.find_element(*RegistrationPage.email_identifier)
        elem.clear()
        elem.send_keys(email_id)

    def set_password(self, password):
        elem = self.wd.find_element(*RegistrationPage.password_confirm_identifier)
        elem.clear()
        elem.send_keys(password)


class RegistrationSuccessPage(BasePage):
    url = 'https://dev.smartresponse.org/registration-success'
