#TASK 3 - PASSWORD GENERATOR

import secrets
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password = ''.join(secrets.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))

        if password_length < 6:
            print("Password length should be at least 6 characters.")
            return

        password = generate_password(password_length)
        print("Generated Password: ", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
