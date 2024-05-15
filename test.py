# test.pyooo
import re
# email = input("Enter customer email: ")
# print(re.match(r"^\S+@\S+\.\S+$", email))
phone = input("Enter customer phone: ")
pattern = re.match(r'^([0|\+[0-9]{1,5})?([7-9][0-9]{9})$',phone)
print(id(pattern))