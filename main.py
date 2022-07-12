import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no formato: +55xxxxxxxxxxx ')

#convertendo string em número de telefone
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number,'pt'))