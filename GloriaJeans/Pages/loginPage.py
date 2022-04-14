from Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_testbox_xpath = Locators.username_testbox_xpath
        self.password_testbox_xpath = Locators.password_testbox_xpath
        self.login_button_class_name = Locators.login_button_class_name


    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_testbox_xpath).clear()
        self.driver.find_element_by_xpath(Locators.username_testbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_testbox_xpath).clear()
        self.driver.find_element_by_xpath(Locators.password_testbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_class_name).click()

