import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 characters for security.")
                continue
            return length
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_complexity_choice():
    print("\nSelect password complexity:")
    print("1. Simple (lowercase letters only)")
    print("2. Medium (lowercase and uppercase letters)")
    print("3. Strong (letters and numbers)")
    print("4. Very Strong (letters, numbers, and special characters)")
    
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

def get_character_set(complexity):
    character_sets = {
        '1': string.ascii_lowercase,
        '2': string.ascii_lowercase + string.ascii_uppercase,
        '3': string.ascii_letters + string.digits,
        '4': string.ascii_letters + string.digits + string.punctuation
    }
    return character_sets[complexity]

def generate_password(length, character_set, complexity):
    password = []
    
    if complexity == '2':  # Medium
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
    elif complexity == '3':  # Strong
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
    elif complexity == '4':  # Very Strong
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))
        password.append(random.choice(string.punctuation))
    
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(character_set))
    
    random.shuffle(password)
    
    return ''.join(password)

def display_password(password, length, complexity_name):
    print("\n" + "="*50)
    print("           PASSWORD GENERATED")
    print("="*50)
    print(f"Length: {length} characters")
    print(f"Complexity: {complexity_name}")
    print(f"Password: {password}")
    print("="*50)

def get_complexity_name(complexity):
    names = {
        '1': 'Simple',
        '2': 'Medium',
        '3': 'Strong',
        '4': 'Very Strong'
    }
    return names[complexity]

def copy_to_clipboard_prompt(password):
    print(f"\nYour password has been generated!")
    print("Make sure to:")
    print("• Copy and save your password securely")
    print("• Don't share it with anyone")
    print("• Store it in a password manager if possible")

def main():
    print("="*50)
    print("         PASSWORD GENERATOR")
    print("="*50)
    print("Generate strong and secure passwords!")
    
    while True:
        # Get user preferences
        length = get_password_length()
        complexity = get_complexity_choice()
        complexity_name = get_complexity_name(complexity)
        
        character_set = get_character_set(complexity)
        
        # Generate password
        password = generate_password(length, character_set, complexity)
        
        display_password(password, length, complexity_name)
        
        copy_to_clipboard_prompt(password)
        
        while True:
            generate_another = input("\nDo you want to generate another password? (yes/no): ").lower()
            if generate_another in ['yes', 'y']:
                print("\n" + "-"*50)
                break
            elif generate_another in ['no', 'n']:
                print("\nThank you for using the Password Generator!")
                return
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
