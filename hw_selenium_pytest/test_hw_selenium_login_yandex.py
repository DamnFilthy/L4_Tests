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
        time.sleep(1)

        login = self.driver.find_element_by_name('login')
        login.send_keys('Shiryaev12345')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()
        time.sleep(3)

        passwd = self.driver.find_element_by_id('passp-field-passwd')
        passwd.send_keys('1345685Aa')

        time.sleep(1)

        self.driver.find_element(By.XPATH, '//button[span="Войти"]').click()
        time.sleep(3)
        self.assertIn("Яндекс.Паспорт", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
