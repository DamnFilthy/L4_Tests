import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class YandexPassportTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://passport.yandex.ru/auth')

    def test_yandex_login(self):
        # input login
        login = self.driver.find_element_by_name('login')
        login.send_keys('ТУТ_ВАШ_ЛОГИН')
        time.sleep(1)
        # click
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()
        time.sleep(3)
        # input password
        passwd = self.driver.find_element_by_id('passp-field-passwd')
        passwd.send_keys('ТУТ_ВАШ_ПАРОЛЬ')
        time.sleep(1)
        # click
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()
        time.sleep(3)

        self.assertIn("Яндекс.Паспорт", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
