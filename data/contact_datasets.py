import pytest
from faker import Faker

fake =Faker()

PHONE_ALERT_TEXT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid: должно иметь формат адреса электронной почты"

INVALID_CONTACT_FIELDS = [
    pytest.param("phone","0504",PHONE_ALERT_TEXT,id="phone_too_short"),
    pytest.param("phone",fake.numerify("#"*20),PHONE_ALERT_TEXT,id="phone_too_long"),
    pytest.param("phone","jfhkdfghkfdh",PHONE_ALERT_TEXT,id="invalid_phone_number_letters"),
    pytest.param("email","dfsdgsgdgsd",EMAIL_ALERT_TEXT,id="invalid_email_letters"),
    pytest.param("email","invalid_email_format",EMAIL_ALERT_TEXT,id="invalid_email_format"),
    pytest.param("email","כגכק",EMAIL_ALERT_TEXT,id="email_hebrew"),
    pytest.param("email","f@.dfjjg",EMAIL_ALERT_TEXT,id="dot_after_at"),
]

SUCCESS_DESCRIPTIONS = [
    pytest.param(None,id="all_fields"),
    pytest.param("",id="required_fields_only")
]





