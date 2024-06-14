import re

pattern = r'^\d{3}-\d{3}-\d{4}'

str = input("Enter the number :  ")

res = re.match(pattern,str)

if res:
    print("The phone number is valid")
else:
    print("Not valid")