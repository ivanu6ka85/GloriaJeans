from selenium import webdriver
import time
import unittest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage



class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/SkillFactory/GloriaJeans/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get('https://www.gloria-jeans.ru/login')

        login = LoginPage(driver)
        login.enter_username("6arikov85@mail.ru")
        login.enter_password("Kruglik0v85")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ =='__main__':
    unittest.main()

