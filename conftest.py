import pytest
import logging
from selenium import webdriver

from data.contact_data import create_contact
from data.user_data import existing_user
from pages.add_new_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from pages.login_page import LoginPage
from tests.test_login import VALID_EMAIL, VALID_PASSWORD
from utils.logger_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

@pytest.fixture #(scope="function") - чистый браузер (по сути по умолчвнию), session - один браузер, одна сессия логина на все тесты
def driver():
    logger.info("Starting browser session")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #в течение 5 секунд постоянно обращается к браузеру и смотрит появлился ли элемент(по сути относится к find element)
    driver.maximize_window() #на полный экран
    driver.get("https://telranedu.web.app/")

    yield driver
    logger.info("Closing browser session")
    driver.quit()

@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    logger.info(f"Logging in user:{user.username}")

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    return driver

@pytest.fixture
def ensure_min_contacts(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)

    contacts_page.open_contacts_list()
    count = contacts_page.total_contacts_count()
    if count<3:
        logger.warning(f"Contact list has {count} contacts (<3), creating test data")

    while contacts_page.total_contacts_count()<3:
        contact_page.create_contact(create_contact())
        contacts_page.open_contacts_list()
    return authenticated_driver


