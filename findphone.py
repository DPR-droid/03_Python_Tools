# Python Phone Finder
# https://towardsdatascience.com/fetching-mobile-number-details-using-python-79077c2ae4f0

import pyfiglet
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from datetime import datetime

ascii_banner = pyfiglet.figlet_format('PHONE NUMBER FINDER')
print(ascii_banner)
target = input("Mobile no. with country code: ")

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)


location = phonenumbers.parse(target, "CH")
provider = phonenumbers.parse(target, "RO")
print(geocoder.description_for_number(location, "en"))
print(carrier.name_for_number(provider, "en"))
