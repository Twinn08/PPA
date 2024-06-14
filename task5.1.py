def isphonenumber(phone_number):
    if len(phone_number) != 12:
        return False
    for i in range(0, 3):
        if not phone_number[i].isdecimal():
            return False
    if phone_number[3] != '-':
        return False
    for i in range(4, 7):
        if not phone_number[i].isdecimal():
            return False
    if phone_number[7] != '-':
        return False
    for i in range(8, 12):
        if not phone_number[i].isdecimal():
            return False
    return True

phone_number = input("Enter the phone number: ")
print("Is", phone_number, "a valid number? :", isphonenumber(phone_number))
