import phonenumbers
from phonenumbers import geocoder

phonenumbers1 = phonenumbers.parse("NUMARA")
phonenumbers2 = phonenumbers.parse("NUMARA")

print("\nNumarayla Lokasyon belirleme\n")
print(geocoder.description_for_number(phonenumbers1, "tr")); # Burada tr yerine başka dillerin kısaltımını da belirtebilirsiniz.
print(geocoder.description_for_number(phonenumbers2, "tr"));
