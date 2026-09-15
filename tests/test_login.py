import pytest

from data.user_datasets import INVALID_LOGIN_USERS
from pages.login_page import LoginPage

VALID_EMAIL = "ground.control.p@gmail.com"
VALID_PASSWORD = "Qwerty123$"
INVALID_EMAIL = "ground.control.b@gmail.com"
INVALID_PASSWORD = "Qwerty123"

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.is_logged() is True



@pytest.mark.parametrize("user_factory",INVALID_LOGIN_USERS)
def test_login_rejected(driver,user_factory):
    login_page = LoginPage(driver)
    user = user_factory()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

# def test_login_with_wrong_email(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(INVALID_EMAIL)
#     login_page.fill_password(VALID_PASSWORD)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
#
# def test_login_with_wrong_password(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email(VALID_EMAIL)
#     login_page.fill_password(INVALID_PASSWORD)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
#
# def test_login_unregistered_user(driver):
#     login_page = LoginPage(driver)
#
#     login_page.open_login_form()
#     login_page.fill_email("ground.control@gmail.com")
#     login_page.fill_password("Qwerty123#")
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
