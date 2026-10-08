import time
import logging

import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class ContactPage(BasePage):
    ADD_NAV_LINK = (By.CSS_SELECTOR,"[href='/add']")
    NAME_INPUT = (By.CSS_SELECTOR,"input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")
    SAVE_BTN = (By.XPATH,"//button[b[text()='Save']]")
    CONTACT_NAV_LINK=(By.CSS_SELECTOR,"[href='/contacts']")
    CONTACT_CARDS = (By.CLASS_NAME,"contact-item_card__2SOIM")



    @allure.step("Open contact form")
    def open_contact_form(self):
        # self.driver.find_element(*self.ADD_NAV_LINK).click()
        self.click(self.ADD_NAV_LINK)

    @allure.step("Fill the name")
    def fill_name(self,name):
        # self.driver.find_element(*self.NAME_INPUT).clear()
        # self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.fill(self.NAME_INPUT,name)

    @allure.step("Fill the last name")
    def fill_last_name(self,last_name):
        # self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        # self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.fill(self.LAST_NAME_INPUT, last_name)

    @allure.step("Fill the phone")
    def fill_phone(self,phone):
        # self.driver.find_element(*self.PHONE_INPUT).clear()
        # self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.fill(self.PHONE_INPUT, phone)

    @allure.step("Fill the email")
    def fill_email(self,email):
        self.fill(self.EMAIL_INPUT, email)

    @allure.step("Fill the address")
    def fill_address(self,address):
        # self.driver.find_element(*self.ADDRESS_INPUT).clear()
        # self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.fill(self.ADDRESS_INPUT,address)

    @allure.step("Fill the description")
    def fill_description(self,description):
        # self.driver.find_element(*self.DESCRIPTION_INPUT).clear()
        # self.driver.find_element(*self.DESCRIPTION_INPUT).send_keys(description)
        self.fill(self.DESCRIPTION_INPUT,description)

    @allure.step("Fill the contact")
    def fill_contact(self,contact):
        self.fill_name(contact.name)
        self.fill_last_name(contact.last_name)
        self.fill_phone(contact.phone)
        self.fill_email(contact.email)
        self.fill_address(contact.address)
        self.fill_description(contact.description)

    @allure.step("Submit save")
    def submit_save(self):
        self.click(self.SAVE_BTN)

    @allure.step("Check contact card is visible")
    def contact_card_visible(self,phone):
        locator = (By.XPATH,f"//h3[text()='{phone}']")
        element = WebDriverWait(self.driver,timeout=5).until(
            EC.presence_of_element_located(locator)
        )
        return element.is_displayed()

    @allure.step("Open contact details")
    def open_contact_details(self,phone):
        card = self.driver.find_element(By.XPATH,f"//h3[text()='{phone}']/..").click() #/.. - кликаем по родителю
        card.click()

    @allure.step("Check the button is active")
    def is_add_button_active(self):
        add_link = self.find(self.ADD_NAV_LINK)
        return "active" in add_link.get_attribute("class")

    @allure.step("Open contact list")
    def open_contact_list(self):
        self.click(self.CONTACT_NAV_LINK)
        WebDriverWait(self.driver,timeout=5).until(EC.url_contains("/contacts"))
        time.sleep(1)

    # def contact_cards_count(self, phone):
    #     return len(self.driver.find_elements(By.XPATH, f"/h3[text()='{phone}']"))

    @allure.step("Counting contact cards")
    def contact_cards_count(self, phone):
        locator = (By.XPATH, f"//*[contains(text(), '{phone}')]")

        elements = self.driver.find_elements(*locator)
        return len(elements)

    @allure.step("Crate contact")
    def create_contact(self,contact):
        logger.info(f"Creating contact:{contact.phone}")
        self.open_contact_form()
        self.fill_contact(contact)
        self.submit_save()
        time.sleep(3)

