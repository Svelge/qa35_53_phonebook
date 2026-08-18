import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #в течение 5 секунд постоянно обращается к браузеру и смотрит появлился ли элемент(по сути относится к find element)
    driver.maximize_window() #на полный экран
    driver.get("https://telranedu.web.app/")

    yield driver

    driver.quit()

