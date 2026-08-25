import uuid

from models.user import User
from pages.registration_page import RegistrationPage

VALID_EMAIL = "groundcontrolp@gmail.com"
VALID_PASSWORD = "Qwerty123$"

INVALID_EMAIL = "invalid_email_format"
INVALID_PASSWORD = "Qwerty123"

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()
    assert registration_page.is_registered() is True

def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email(INVALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(INVALID_PASSWORD)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        email = "qwerty123gmail.com",
        password = "Qwerty123$"
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_empty_email(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        email = "",
        password = "Qwerty123$"
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        email = f"qwerty_{random_suffix}@gmail.com",
        password = "qw"
    )

    print(random_suffix)
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_empty_password(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        email=f"qwerty_{random_suffix}@gmail.com",
        password=""
    )

    print(random_suffix)
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_empty_fields(driver):
    registration_page = RegistrationPage(driver)
    user = User(
        email = "",
        password = ""
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_success_1(driver):
    registration_page = RegistrationPage(driver)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        email=f"qwerty_{random_suffix}@gmail.com",
        password="Qwerty123$"
    )

    print(random_suffix)
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()
    assert registration_page.is_registered() is True