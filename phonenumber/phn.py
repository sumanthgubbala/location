import phonenumbers
from test import number 
from phonenumbers import geocoder
from phonenumbers import carrier
phn =phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(phn,"en"))
ser =phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ser,"en"))
