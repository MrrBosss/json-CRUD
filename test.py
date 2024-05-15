# test.pyooo
# import re
# email = input("Enter customer email: ")
# print(re.match(r"^\S+@\S+\.\S+$", email))
from pywebio.output import *
import re

def check_phonenumber(num):
    pattern = re.match(r"^[+]{1}(?:[0-9\\-\\(\\)\\/" \
              "\\.]\\s?){6,15}[0-9]{1}$",num)
    if pattern is None:
        print ("Invalid!")
    else:
        print("Valid")

check_phonenumber('+998908232534')