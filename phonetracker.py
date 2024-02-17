import phonenumbers
from test import number  # Assuming you have a valid phone number in the 'number' variable

from phonenumbers import geocoder, carrier

# Example for geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# Example for carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
