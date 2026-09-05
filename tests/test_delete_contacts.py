from pages.contacts_page import ContactsPage


def test_delete_one_contact(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()

    count_before = contacts_page.total_contacts_count()
    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()
    count_after = contacts_page.total_contacts_count()

    assert count_after == count_before-1



def test_remove_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()

    assert contacts_page.total_contacts_count() == 0