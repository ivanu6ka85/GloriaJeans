class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = "/html/body/div[6]/div/header/div[2]/div[6]/div/div/div/a[1]"
        self.logout_link_xpath = "/html/body/div[6]/div/header/div[2]/div[6]/div/div/div/a[4]"


    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()