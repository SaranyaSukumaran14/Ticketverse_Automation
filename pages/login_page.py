from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import BASE_URL


class LoginPage(BasePage):

    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[@class='login-btn']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@class='login-button']")

    def open_website(self):
        self.driver.get(BASE_URL)

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BTN)

    def login(self, email, password):
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)