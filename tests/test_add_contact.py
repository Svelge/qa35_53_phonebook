import logging

import pytest
from faker import Faker

from data.contact_data import create_contact
from data.contact_datasets import INVALID_CONTACT_FIELDS, SUCCESS_DESCRIPTIONS
from pages.add_new_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
logger = logging.getLogger(__name__)


@pytest.mark.parametrize("description", SUCCESS_DESCRIPTIONS)
def test_add_contact_success_all_fields(authenticated_driver,description):
    logger.info("Test: test_add_contact_success_all_fields")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact() if description is None else create_contact(SUCCESS_DESCRIPTIONS)

    contact_page.create_contact(contact)

    assert contacts_page.contact_card_visible(contact.phone)




# def test_add_contact_success_req_fields(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#
#     contact = create_contact(description="")
#     contact_page.create_contact(contact)
#
#     assert contacts_page.contact_card_visible(contact.phone)




def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(name = "")

    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0




def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(last_name="")


    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0



#@pytest.mark.skip(reason = "BUG-123: Contact with empty mail")
@pytest.mark.xfail (reason = "BUG-123: Contact with empty mail")
def test_add_contact_empty_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(email="")

    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(address="")


    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0


@pytest.mark.regression
@pytest.mark.parametrize("field,value,expected_alert",INVALID_CONTACT_FIELDS)
def test_add_contact_invalid_field_rejected(authenticated_driver,field,value,expected_alert):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(**{field: value})

    contact_page.create_contact(contact)

    assert contact_page.get_alert_text().strip() == expected_alert
    contact_page.accept_alert()
    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

# def test_add_contact_invalid_phone_too_long(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone=fake.numerify("#"*20))
#
#     contact_page.create_contact(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0
#
# def test_add_contact_invalid_phone_letters(authenticated_driver):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(phone="jfhkdfghkfdh")
#
#     contact_page.create_contact(contact)
#
#
#     assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
#     contact_page.accept_alert()
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0


# def test_add_contact_invalid_email(authenticated_driver,field,value,expected_alert):
#     contact_page = ContactPage(authenticated_driver)
#     contacts_page = ContactsPage(authenticated_driver)
#     contact = create_contact(**{field: value})
#
#     contact_page.create_contact(contact)
#
#     assert contact_page.get_alert_text().strip() == expected_alert
#     contact_page.accept_alert()
#
#     assert contact_page.is_add_button_active()
#
#     contacts_page.open_contacts_list()
#     assert contacts_page.contact_cards_count(contact.phone) == 0


@pytest.mark.xfail (reason = "BUG-124: Duplicate phone")
def test_add_contact_duplicate_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    shared_phone = fake.unique.numerify("050##########")
    first_contact = create_contact(phone=shared_phone)
    second_contact = create_contact(phone=shared_phone)

    contact_page.create_contact(first_contact)
    assert contacts_page.contact_card_visible(shared_phone)

    contact_page.create_contact(second_contact)


    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(shared_phone) == 1

# pytest -v -m smoke/regression / pytest -v -m "regression and not smoke"