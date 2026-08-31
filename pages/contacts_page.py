import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ContactsPage(BasePage):
    CONTACTS_NAV_LINK = (By.CSS_SELECTOR, "[href='/contacts']")
    CONTACT_CARDS = (By.CLASS_NAME,"contact-item_card__2SOIM")

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


    def open_contact_details(self, phone):
        # Кликает по карточке контакта с данным телефоном (родитель h3) —
        # переходит на страницу деталей /contacts/:id.
        locator = (By.XPATH, self.CONTACT_CARDS)
        self.click(locator)