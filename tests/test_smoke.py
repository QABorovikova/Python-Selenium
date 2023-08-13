import pytest

from selenium.webdriver.common.by import By

URL = "https://testqastudio.me/"

def test_smoke(browser):
    """ test-1 """
    
   # определяем адрес страницы для теста и переходим на неё
    browser.get(url=URL)
		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="tab-best_sellers"]')
    element.click()
		# ищем по селектору карточку "ЭЛЛЬБИ Подвесная лампа" и кликаем по нему,
        # чтобы просмотреть детали
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'BFB9ZOK210', "Unexpected sku"