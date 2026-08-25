import random

from faker import Faker

from models.contact import Contact
from pages.add_contact_page import ContactPage

fake = Faker()

def test_add_contact_success_req_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    # random_suffix = random.randint(1,1000000)

    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        phone = fake.numerify("050#########"),
        # phone = f"05035{random_suffix}",
        email = fake.unique.email(),
        address = fake.street_address(),
        description = fake.sentence(nb_words=5)
    )

    # print(random_suffix)

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_save()

    assert contact_page.contact_card_visible(contact.phone)

