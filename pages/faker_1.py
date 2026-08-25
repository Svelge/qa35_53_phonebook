from faker import Faker

fake = Faker()

print(fake.first_name())
print(fake.last_name())
print(fake.email())
print(fake.phone_number())
print(fake.street_address())
print(fake.sentence())
print(fake.numerify(text="05##########"))