import logging

import allure

from pages.contacts_page import ContactsPage

logger = logging.getLogger(__name__)

@allure.story("Delete contact success")
@allure.title("Deleting one contact")
def test_delete_one_contact(ensure_min_contacts):
    logger.info("Test: delete first contact")
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()

    count_before = contacts_page.total_contacts_count()
    logger.info(f"Contact before delete: {count_before}")
    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()
    count_after = contacts_page.total_contacts_count()
    logger.info(f"Contacts after delete: {count_after}")

    assert count_after == count_before-1


@allure.story("Delete contact success")
@allure.title("Removing all contacts")
def test_remove_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()

    assert contacts_page.total_contacts_count() == 0