from selenium import webdriver
from selenium.webdriver.common.by import By
from general import Helpers
from cred import mycredentials


class Registration(Helpers):
    URL = "https://courses.letskodeit.com/"
    signinnow = (By.XPATH, "//div[@class='sbpro-bg-styler text-center']//div//a")
    first_name = (By.XPATH, "//input[@id ='name' and @class ='form-control input-md']")
    last_name = (By.XPATH, "//input[@id='last_name']")
    email_add = (By.XPATH, "//input[@id='email' and @class='form-control input-md']")
    password = (By.XPATH, "//input[@id='password']")
    confirm_password = (By.XPATH, "//input[@id='password_confirmation']")
    sign_up = (By.XPATH, "//div[@class='col-xs-12 col-md-12']//input")

    def input_fields(self):
        self.browser.find_element(*self.signinnow).click()
        self.browser.find_element(*self.first_name).send_keys(mycredentials['myname'])
        self.browser.find_element(*self.last_name).send_keys(mycredentials['mysurname'])
        self.browser.find_element(*self.email_add).send_keys(mycredentials['myemail'])
        self.browser.find_element(*self.assword).send_keys(mycredentials['mypassword'])
        self.browser.find_element(*self.confirm_password).send_keys(mycredentials['mypassword'])
        self.browser.find_element(*self.sign_up).click()


