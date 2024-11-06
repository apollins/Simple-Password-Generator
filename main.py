# -*- coding: utf-8 -*-
import random
import string
from controllers import insert_password
import bcrypt


list_letters_lowercase = string.ascii_lowercase
list_letters_uppercasecase = string.ascii_uppercase
list_digits = string.digits
list_special_characters = string.punctuation

user_name = str(input("Enter a name: "))
mes_1 = int(input("Enter the password length: "))
if mes_1 < 4:
    print("The password must be longer than 4 characters. Try again.")
else:
    pass

need_uppercase = False
need_lowercase = False
need_digit = False
need_characters = False

while True:
    mes_2 = input("Do you need uppercase letters? (yes/no) \n").strip().lower()
    if mes_2 == 'yes':
        need_uppercase = True
        break
    elif mes_2 == 'no':
        need_uppercase = False
        break
    else:
        print('Invalid input. Please enter "yes" or "no".')

while True:
    mes_2 = input("Do you need lowercase letters? (yes/no) \n").strip().lower()
    if mes_2 == 'yes':
        need_lowercase = True
        break
    elif mes_2 == 'no':
        need_lowercase = False
        break
    else:
        print('Invalid input. Please enter "yes" or "no".')

while True:
    mes_4 = str(input("Do you need numbers? (yes/no) \n")).strip().lower()
    if mes_4 == 'yes':
        need_digit = True
        break
    elif mes_4 == 'no':
        need_digit = False
        break
    else:
        print('Invalid input. Please enter "yes" or "no".')

while True:
    mes_5 = str(input("Do you need special characters? (yes/no) \n")).strip().lower()
    if mes_5 == 'yes':
        need_characters = True
        break
    elif mes_5 == 'no':
        need_characters = False
        break
    else:
        print('Invalid input. Please enter "yes" or "no".')


password_pool = []
if need_uppercase:
    password_pool.append(list_letters_uppercasecase)
if need_lowercase:
    password_pool.append(list_letters_lowercase)
if need_digit:
    password_pool.append(list_digits)
if need_characters:
    password_pool.append(list_special_characters)

final_password = []

for i in password_pool:
    final_password.append(random.choice(i))

additional_length = mes_1 - len(final_password)

if additional_length > 0:
    all_characters = ''.join(password_pool)
    final_password += random.choices(all_characters, k=additional_length)

random.shuffle(final_password)

user_password = ''.join(final_password)
print("Generated password:", user_password + '.')

category_count = sum([need_uppercase, need_lowercase, need_digit, need_characters])
if mes_1 >= 12 and category_count >= 3:
    strength = "high"
elif mes_1 >= 8 and category_count >= 2:
    strength = "medium"
else:
    strength = "low"
print(f"Password reliability - {strength}.")

hashed_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
print(hashed_password)
print(hashed_password.decode())

insert_password(user_name, user_password, hashed_password, strength)