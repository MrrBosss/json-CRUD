# test.pyooo
# import re
# email = input("Enter customer email: ")
# print(re.match(r"^\S+@\S+\.\S+$", email))


# import re

# def check_phonenumber(num):
#     pattern = re.match(r"^[+]{1}(?:[0-9\\-\\(\\)\\/" \
#               "\\.]\\s?){6,15}[0-9]{1}$",num)
#     if pattern is None:
#         print ("Invalid!")
#     else:
#         print("Valid")

# check_phonenumber('+998908232534')
from pywebio.output import *
popup('popup title', 'popup text content', size=PopupSize.SMALL)

popup('Popup title', [
    put_html('<h3>Popup Content</h3>'),
    'html: <br/>',
    put_table([['A', 'B'], ['C', 'D']]),
    put_buttons(['close_popup()'], onclick=lambda _: close_popup())
])