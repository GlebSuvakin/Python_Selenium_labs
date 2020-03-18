import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sec = 1


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        # Зададим драйвер нашего браузера
        self.driver = webdriver.Chrome('C:/Users/kapit/source/python/chromedriver.exe')
        self.driver.get('https://web2.0calc.ru')

    def tearDown(self):
        self.driver.close()

    def cooki(self):
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'cookieconsentallowall')))
        elem.click()

    def getInput(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/input[2]")))

    def getOutput(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'input')))

    # проверка работы калькулятора
    def test_01(self):
        driver = self.driver
        self.cooki()
        elem = self.getInput()
        elem.send_keys('1' + Keys.SHIFT + '+')
        elem.send_keys('1' + Keys.ENTER)
        time.sleep(sec)
        elem = self.getOutput()
        assert '2' == elem.get_attribute('value')
        print('test_01 - Complite!')

    # проверка ввода через интерфейс калькулятора
    def test_02(self):
        driver = self.driver
        self.cooki()
        elem = driver.find_element_by_id('Btn7')
        elem.click()
        elem = driver.find_element_by_id('Btn0')
        elem.click()
        elem = driver.find_element_by_id('BtnDiv')
        elem.click()
        elem = driver.find_element_by_id('Btn7')
        elem.click()
        elem = driver.find_element_by_id('BtnCalc')
        elem.click()
        time.sleep(sec)
        elem = self.getOutput()
        assert '10' == elem.get_attribute('value')
        print('test_02 - Complite!')

    # проверка ввода с клавиатуры
    def test_03(self):
        driver = self.driver
        self.cooki()
        action = ActionChains(driver)
        action.send_keys('2').key_down(Keys.SHIFT).send_keys('+').key_up(Keys.SHIFT).send_keys(
            '2' + Keys.ENTER).perform()
        time.sleep(sec)
        elem = self.getOutput()
        assert '4' == elem.get_attribute('value')
        print('test_03 - Complite!')

    # проверка вычисления сложного выражения комбинированным вводом
    def test_04(self):
        driver = self.driver
        self.cooki()
        action = ActionChains(driver)
        action.send_keys('2^3').key_down(Keys.SHIFT).send_keys('*').key_up(Keys.SHIFT).send_keys('2+2').perform()
        elem = driver.find_element_by_id('BtnCalc')
        elem.click()
        time.sleep(sec)
        elem = self.getOutput()
        assert '18' == elem.get_attribute('value')
        print('test_04 - Complite!')

    # проверка работы истории калькулятора
    def test_05(self):
        driver = self.driver
        self.cooki()
        action = self.getInput()
        action.send_keys('sin(30)' + Keys.ENTER)
        time.sleep(sec)
        elem = driver.find_element_by_id('BtnClear')
        elem.click()
        time.sleep(sec)
        action.send_keys('3^3' + Keys.ENTER)
        time.sleep(sec)
        elem = driver.find_element_by_class_name('btn.dropdown-toggle.pull-right')
        elem.click()
        time.sleep(sec)
        elem = driver.find_elements_by_tag_name('p')
        for i in elem:
            if i.get_attribute('title') == 'sin(30)':
                i.click()
                elem = driver.find_element_by_id('BtnCalc')
                elem.click()
                time.sleep(sec)
                break
        elem = self.getOutput()
        assert '0.5' == elem.get_attribute('value')
        print('test_05 - Complite!')


if __name__ == "__main__":
    unittest.main()
