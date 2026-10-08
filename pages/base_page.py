import logging

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
logger = logging.getLogger(__name__)



class BasePage:
    def __init__(self,driver):
        self.driver = driver

    @allure.step("Find")
    def find(self,locator):
        return self.driver.find_element(*locator)
    @allure.step("Click")
    def click(self,locator):
        logger.info(f"Click on {locator}")
        self.wait_until_clickable(locator).click()
    @allure.step("Fill")
    def fill(self,locator,value):
        logger.info(f"Fill {locator} with {value}")
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

        # self.find(locator).clear()
        # self.find(locator).send_keys(value)

    @allure.step("Get alert text")
    def get_alert_text(self):
        alert = WebDriverWait(self.driver,timeout=10).until(
            EC.alert_is_present()
        )
        return alert.text

    @allure.step("Accept alert")
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    @allure.step("Wait until element is visible")
    def wait_until_visible(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Wait until element is clickable")
    def wait_until_clickable(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Wait until url matches")
    def wait_until_url_matches(self,locator,timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.url_matches(locator))

    def wait_until_alert_present(self,timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.alert_is_present())
