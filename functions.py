import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password_length = 12 # Define the length of the password
password = "" # Initialize an empty string to store the password
for index in range(password_length):
    password += random.choice(characters)
print(f"Password generated: {password}")
