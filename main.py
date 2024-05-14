# Certainly! Here's an extended version of a task to reinforce working with JSON and text files:

# Task: Managing Customer Data
# You've been assigned to create a program that manages customer data for a small business. The program should allow the user to perform the following tasks:

# Add a New Customer: Add a new customer to the database. The customer data should include:
# Name
# Email
# Phone Number
# Address
# Update Customer Information: Update the information of an existing customer. The user should be able to update any of the customer's details.
# Delete a Customer: Remove a customer from the database based on their email address.
# Search for a Customer: Search for a customer by their email address and display their information.
# Display All Customers: Display the information of all customers in the database

from functions import *
from pywebio.input import input
from pywebio.output import put_text

def main():
    file_name = "customers.json"
    customers = load_customers(file_name)
    while True:
        put_text("1. Add a new customer")
        put_text("2. Update customer information")
        put_text("3. Delete a customer")
        put_text("4. Search for a customer")
        put_text("5. Display all customers")
        put_text("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_customer(customers, file_name)
        elif choice == "2":
            update_customer(customers,file_name)
        elif choice == "3":
            delete_customer(customers, file_name)
        elif choice == "4":
            search_customer(customers)
        elif choice == "5":
            display_customers(customers)
        elif choice == "6":
            break
        else:
            put_text("Invalid option. Please choose again!!")

if __name__=="__main__":
    main()

