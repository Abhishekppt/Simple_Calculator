import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

   
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8. Please try again.")
                continue
            
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break
        
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
