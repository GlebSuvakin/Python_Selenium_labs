import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        # Зададим драйвер нашего браузера
        self.driver = webdriver.Chrome('C:/Users/kapit/source/python/chromedriver.exe')
        self.driver.get('https://google.com')

    def test_01(self):
        driver = self.driver
        # список элементов с тегом 'a'
        TAG_A = driver.find_elements_by_tag_name('a')
        # удаление элементов без атрибута 'href'
        for i in TAG_A:
            if i.get_attribute('href') == None:
                TAG_A.remove(i)
        # заполнение списка ссылок
        sites = []
        for i in TAG_A:
            sites.append(i.get_attribute('href'))
        sites = [i for i in sites if i != None]
        sites1 = sorted(sites)
        # открытие ссылок из сортированного списка в новой вкладке
        k = [0] * len(sites)
        for i in range(0, len(sites), 1):
            print(sites1[i])
            driver.execute_script("window.open()")
            driver.switch_to.window(driver.window_handles[i + 1])
            driver.get(sites1[i])
            # заполнение списка индексов открытых окон
            for j in range(0, len(sites), 1):
                if sites[j] == sites1[i]:
                    k[j] = i
                    break
            time.sleep(1)
        print()
        # вывод исходого списка ссылок
        print('Исходный список ссылок:')
        for i in range(len(sites)):
            print(sites[i])
        print()
        # закрытие первого сайта
        driver.switch_to.window(driver.window_handles[0])
        print('Close the first window: ', driver.title)
        time.sleep(1)
        driver.close()
        print()
        # закрытие всех сайтов в порядке первоначального списка
        for i in range(0, len(sites), 1):
            print('Close: ', sites[i])
            driver.switch_to.window(driver.window_handles[k[i]])
            for j in range(0, len(k), 1):
                if k[j] > k[i]:
                    k[j] -= 1
            time.sleep(1)
            driver.close()
            time.sleep(1)


if __name__ == "__main__":
    unittest.main()
