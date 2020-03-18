import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VKTest(unittest.TestCase):

    def setUp(self):
        # Зададим драйвер нашего браузера
        self.driver = webdriver.Chrome('C:/Users/kapit/source/python/chromedriver.exe')
        self.driver.get('https://vk.com')

    def tearDown(self):
        self.driver.close()

    def test_01(self):
        driver = self.driver
        # находим строчки ввода email, password и кнопку Вход
        email = driver.find_element_by_xpath('//*[@id=\'index_email\']')
        password = driver.find_element_by_xpath('//*[@id=\'index_pass\']')
        loginButton = driver.find_element_by_xpath('//*[@id=\'index_login_button\']')
        # из файла берем логин и пароль
        resource = open('./login.txt').readlines()
        # заполняем логин и пароль
        email.send_keys(resource[0])
        password.send_keys(resource[1])
        loginButton.click()
        # находим вкладку "Друзья"
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[11]/div/div/div[2]/div[1]/div/nav/ol/li[4]/a/span/span[2]')))
        elem.click()
        # находим вкладку "Друзья онлайн"
        elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Друзья онлайн')))
        elem.click()
        friendsListOnlin = driver.find_elements_by_class_name("friends_field.friends_field_title")
        # берем из списка friendsListOnlin только имена
        friends = [i.text for i in friendsListOnlin]
        print('\tДрузья онлайн:')
        print('\n'.join(friends))


if __name__ == "__main__":
    unittest.main()
