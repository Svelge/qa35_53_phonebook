import pytest
from faker import Faker

from data.contact_data import create_contact
from pages.add_new_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()

def test_edit_contact_name_update(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contacts_page=ContactsPage(authenticated_driver)

    contact=create_contact()
    contact_page.create_contact(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME_INPUT,new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_by_phone(contact.phone) == new_name

def test_edit_contact_last_name_update(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contacts_page=ContactsPage(authenticated_driver)

    contact=create_contact()
    contact_page.create_contact(contact)
    new_last_name = fake.last_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME_INPUT,new_last_name)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    actual_last_name = contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME_INPUT)
    assert actual_last_name == new_last_name

def test_edit_contact_phone_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_phone = fake.unique.numerify("050#######")

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_card_visible(new_phone)
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_edit_contact_email_updated(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contacts_page=ContactsPage(authenticated_driver)

    contact=create_contact()
    contact_page.create_contact(contact)
    new_email = fake.unique.email()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT,new_email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    actual_email =  contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT)
    assert actual_email == new_email

def test_edit_contact_address_updated(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contacts_page=ContactsPage(authenticated_driver)

    contact=create_contact()
    contact_page.create_contact(contact)
    new_address = fake.city()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS_INPUT,new_address)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    actual_address = contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS_INPUT)
    assert actual_address == new_address

@pytest.mark.skip(reason="BUG-125: Object undefined")
def test_edit_contact_description_updated(authenticated_driver):
    contact_page=ContactPage(authenticated_driver)
    contacts_page=ContactsPage(authenticated_driver)

    contact=create_contact()
    contact_page.create_contact(contact)
    new_description = fake.sentence()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_DESCRIPTION_INPUT,new_description)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    actual_description = contacts_page.get_edit_contact(contacts_page.EDIT_DESCRIPTION_INPUT)
    assert actual_description == new_description


def test_edit_contact_empty_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME_INPUT, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_name_by_phone(contact.phone) == contact.name


def test_edit_contact_empty_last_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME_INPUT, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME_INPUT) == contact.last_name


def test_edit_contact_empty_phone_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT, "")
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_count(contact.phone) == 1


def test_edit_contact_empty_email_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT) == contact.email


def test_edit_contact_empty_address_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS_INPUT, "")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.edit_contact_details()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS_INPUT) == contact.address



@pytest.mark.skip(reason="BUG-126: Duplicate phone accepted after editing")
def test_edit_contact_duplicate_phone_negative(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    existing_contact = create_contact()
    other_contact = create_contact()
    contact_page.create_contact(existing_contact)
    contact_page.create_contact(other_contact)

    contacts_page.open_contact_details(other_contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT, existing_contact.phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_count(existing_contact.phone) == 1

@pytest.mark.skip(reason="BUG-127: Duplicate email accepted after editing")
def test_edit_contact_duplicate_email_negative(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    existing_contact = create_contact()
    other_contact = create_contact()

    contact_page.create_contact(existing_contact)
    contact_page.create_contact(other_contact)

    contacts_page.open_contact_details(other_contact.phone)
    contacts_page.edit_contact_details()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT, existing_contact.email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(other_contact.phone)
    contacts_page.edit_contact_details()

    actual_email = contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT)
    assert actual_email == other_contact.email