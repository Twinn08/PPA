import re

def find_phone_numbers_and_emails(file_path):
    # Define the regex patterns for phone numbers and email addresses
    phone_pattern = r'\+\d{12}'  # Pattern for phone numbers in the format +919900889977
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'  # Pattern for email addresses

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Find all phone numbers and email addresses
    phone_numbers = re.findall(phone_pattern, content)
    email_addresses = re.findall(email_pattern, content)

    return phone_numbers, email_addresses


file_path = input("Enter the path of the file: ")
phone_numbers, email_addresses = find_phone_numbers_and_emails(file_path)

print("Phone Numbers found:")
for phone_number in phone_numbers:
    print(phone_number)

print("\nEmail Addresses found:")
for email in email_addresses:
    print(email)
