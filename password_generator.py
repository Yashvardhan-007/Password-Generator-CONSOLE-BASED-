import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters available to generate password!")

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Welcome to the Password Generator 🔐")
    
    
    length = int(input("Enter password length (default 12): ") or 12)
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"
    count = int(input("How many passwords to generate?: ") or 1)

    print("\nGenerated Password(s):")
    for i in range(count):
        print(f"{i+1}. {generate_password(length, use_upper, use_digits, use_symbols)}")


if __name__ == "__main__":
    main()
