import random
import string

length = int(input("Enter the desired password length: "))

if length < 3:
    print("Password length must be at least 3.")
else:
    password_chars = [
        random.choice(string.ascii_uppercase),  # One uppercase letter
        random.choice(string.ascii_lowercase),  # One lowercase letter
        random.choice(string.digits)            # One digit
    ]
    
    all_chars = string.ascii_letters + string.digits

    for _ in range(length - 3):
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    
    password = ''.join(password_chars)
    
    # Print the generated password.
    print("Generated Password:", password)
