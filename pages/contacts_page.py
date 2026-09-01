import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ContactsPage(BasePage):
    CONTACTS_NAV_LINK = (By.CSS_SELECTOR, "[href='/contacts']")
    CONTACT_CARDS = (By.CLASS_NAME,"contact-item_card__2SOIM")
    EDIT_BTN = (By.XPATH,"//button[text()='Edit']")
    EDIT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='desc']")
    EDIT_SAVE_BTN = (By.XPATH,"//button[text()='Save']")





    def open_contacts_list(self):
        # Переходит на страницу /contacts по ссылке в навигации и ждёт смены
        # URL плюс небольшую паузу, чтобы список карточек успел отрисоваться
        self.click(self.CONTACTS_NAV_LINK)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/contacts"))
        time.sleep(1)


    def contact_cards_count(self, phone):
        # Считает, сколько карточек контактов с данным телефоном сейчас
        # отображено на странице.
        # Используется, чтобы проверить отсутствие
        # контакта (0 = не сохранился) или дубликаты (>1 = один и тот же
        # телефон сохранён больше одного раза).
        return len(self.driver.find_elements(By.XPATH, f"//h3[text()='{phone}']"))


    def contact_card_visible(self, phone):
        # Ждёт появления карточки с данным телефоном и проверяет, что она
        # видима на странице — используется сразу после сохранения контакта,
        # чтобы убедиться, что он реально появился в списке.
        locator = (By.XPATH, f"//h3[text()='{phone}']")
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))
        return element.is_displayed()


    def open_contact_details(self,phone):
        locator = (By.XPATH, f"//h3[text()='{phone}']")
        self.click(locator)

    def edit_contact_details(self):
        self.click(self.EDIT_BTN)

    def set_edit_field(self,locator,value):
        self.fill(locator,value)

    def submit_edit(self):
        self.click(self.EDIT_SAVE_BTN)
        time.sleep(3)

    def contact_name_by_phone(self, phone):
        card = self.driver.find_element(By.XPATH, f"//h3[text()='{phone}']/..")

        name_element = WebDriverWait(card, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        return name_element.text

    def get_edit_contact(self, locator):
        return self.find(locator).get_attribute("value")