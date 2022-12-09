from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpBasePage
from utils.locators import *
import unittest


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        self.driver = driver
        # super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def click_login_button(self):
        """Tri"""
        login_btn = self.find_element(*self.locator.LOGIN_BUTTON)
        login_btn.click()
    # def search_item(self, item):
    #     self.find_element(*self.locator.SEARCH).send_keys(item)
    #     self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)
    #     return self.find_element(*self.locator.SEARCH_LIST).text


    # def click_sign_in_button(self):
    #     self.find_element(*self.locator.LOGIN).click()
    #     return LoginPage(self.driver)

if __name__ == "__main__":
    unittest.main()
