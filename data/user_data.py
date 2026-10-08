from faker import Faker

from models.user import User
from utils.config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD

fake = Faker()


def create_user(username=None, password=None):
    return User(
        username=username if username is not None else fake.unique.email(),
        password=password if password is not None else fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )


INVALID_EMAIL = "ground.control.bmail.com"
INVALID_PASSWORD = "Qwerty123"


def existing_user():
    return create_user(username=EXISTING_USER_EMAIL, password=EXISTING_USER_PASSWORD)

def invalid_email_user():
    return create_user(username=INVALID_EMAIL, password=EXISTING_USER_PASSWORD)

def invalid_password_user():
    return create_user(username=EXISTING_USER_EMAIL, password=INVALID_PASSWORD)
