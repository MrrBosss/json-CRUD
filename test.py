# test.pyooo
import re
email = input("Enter customer email: ")
print(re.match(r"^\S+@\S+\.\S+$", email))