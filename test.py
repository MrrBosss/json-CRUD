# test.pyooo
import re
# email = input("Enter customer email: ")
# print(re.match(r"^\S+@\S+\.\S+$", email))
phone = input("Enter customer email: ")
pattern = re.match(r"^[+]{1}(?:[0-9\\-\\(\\)\\/\\.]\\s?){6,15}[0-9]{1}$",phone)
print(pattern)