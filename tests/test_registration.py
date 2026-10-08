import logging
import uuid

import allure
import pytest

from data.user_data import create_user
from models.user import User
from pages.registration_page import RegistrationPage
from utils.config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

logger = logging.getLogger(__name__)

@pytest.mark.smoke
@pytest.mark.regression
@allure.story("Registration success")
@allure.title("Registration with valid data")
def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    user = create_user()

    logger.info("Testing successful registration: username=%s", user.username)

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()
    assert registration_page.is_registered() is True

@allure.story("Registration failed")
@allure.title("Registration with wrong email")
def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(username="qfjeigmail.ru")

    logger.info("Testing rejected registration with wrong email: username=%s", user.username)

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with wrong password")
def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(password="qw")
    logger.info("Testing rejected registration with wrong password: password=%s", user.password)

    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with existing data")
def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)
    user = create_user(username=EXISTING_USER_EMAIL,password=EXISTING_USER_PASSWORD)
    logger.info("Testing registration of existing user: username=%s", user.username)
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with email without @")
def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        username = "qwerty123gmail.com",
        password = "Qwerty123$"
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with empty email")
def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        username = "",
        password = "Qwerty123$"
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with short password")
def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        username = f"qwerty_{random_suffix}@gmail.com",
        password = "qw"
    )

    print(random_suffix)
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with empty password")
def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        username=f"qwerty_{random_suffix}@gmail.com",
        password=""
    )

    print(random_suffix)
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration failed")
@allure.title("Registration with empty fields")
def test_registration_with_empty_fields(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        username = "",
        password = ""
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

@allure.story("Registration success_1")
@allure.title("Registration with correct data(2nd test)")
def test_registration_success_1(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        username=f"qwerty_{random_suffix}@gmail.com",
        password="Qwerty123$"
    )

    print(random_suffix)
    registration_page.open_registration_form()
    registration_page.fill_email(user.username)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()
    assert registration_page.is_registered() is True