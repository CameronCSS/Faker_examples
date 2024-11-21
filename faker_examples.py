from faker import Faker

# Create a Faker instance
fake = Faker()

# Various Faker methods
print("PERSONAL INFORMATION:")

print(f"Name: {fake.name()}")
print(f"First Name: {fake.first_name()}")
print(f"Last Name: {fake.last_name()}")
print(f"Prefix: {fake.prefix()}")
print(f"Suffix: {fake.suffix()}")
print(f"Age: {fake.random_int(min=18, max=90)}")
print(f"Favorite words: {fake.sentence(nb_words=7)}") # Not really a sentence just random words



print("\nCONTACT INFORMATION:")

print(f"Email: {fake.email()}")
print(f"Phone Number: {fake.basic_phone_number()}")
print(f"Company Email: {fake.company_email()}")



print("\nADDRESS INFORMATION:")

print(f"Street Address: {fake.street_address()}")
print(f"City: {fake.city()}")
print(f"State: {fake.state()}")
print(f"Zip Code: {fake.postcode()}")
print(f"Country: {fake.country()}")
print(f"Full Address: {fake.address()}")



print("\nJOB/COMPANY INFORMATION:")

print(f"Job Title: {fake.job()}")
print(f"Company Name: {fake.company()}")
print(f"Company Suffix: {fake.company_suffix()}")



print("\nFINANCIAL INFORMATION:")

print(f"Credit Card Number: {fake.credit_card_number()}")
print(f"Credit Card Provider: {fake.credit_card_provider()}")
print(f"Bank Routing number: {fake.aba()}")
print(f"Bank Account number: {fake.bban()}")
print(f"International Account number: {fake.iban()}")
print(f"Currency: {fake.currency_name()}")



print("\nDATE AND TIME:")

print(f"Date of Birth: {fake.date_of_birth(minimum_age=18, maximum_age=90)}")
print(f"Future Date: {fake.future_date()}")
print(f"Past Date: {fake.past_date()}")



print("\nINTERNET AND TECHNOLOGY:")

print(f"Username: {fake.user_name()}")
print(f"Password: {fake.password()}")
print(f"Domain Name: {fake.domain_name()}")
print(f"IPv4: {fake.ipv4()}")
print(f"User Agent: {fake.user_agent()}")



print("\nMISCELLANEOUS:")

print(f"Color: {fake.color_name()}")
print(f"Hex Color: {fake.hex_color()}")
print(f"UUID: {fake.uuid4()}")
print(f"Language: {fake.language_name()}")
print(f"Coupon Code: {fake.bothify(text='????#####??', letters='ABCDF')}")
