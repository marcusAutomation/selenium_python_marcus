from selenium.webdriver.common.by import By


# for maintainability, we can separate web objects by page name

class MainPageLocators(object):
    LOGO = (By.XPATH, '//*[@id="main-header"]/nav/a')
    REGISTER = (By.XPATH, '//*[@id="navigationContent"]/div[1]/a[1]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="navigationContent"]/div[1]/a[2]')


class LoginPageLocators(object):
    CONTINUE_EMAIL_BTN = (By.ID, 'emailContinue-btn1')
    # EMAIL = (By.ID, '#email-continue1 > form > :nth-child(2) > #exampleInputEmail1')
    # PASSWORD = (By.ID, 'ap_password')
    # SUBMIT = (By.ID, 'signInSubmit-input')
    # ERROR_MESSAGE = (By.ID, 'message_error')
