import secrets
import string


def generate_password(length: int, complexity: int, base_word: str = "") -> str:
    """ 
    Generates a password based on the provided length, complexity, and base word.

    Parameters:
    - length (int): The desired length of the password.
    - complexity (int): The desired complexity level (1, 2, 3, or 4).
    - base_word (str): A word that will be integrated into the generated password.

    Returns:
    - A string containing the generated password.
    """
    if not 1 <= complexity <= 4:
        raise ValueError("Complexity must be 1, 2, 3, or 4.")
    
    if length < len(base_word):
        raise ValueError("The password length cannot be smaller than the length of the base word.")

    # Define characters according to the complexity
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 4:
        # Maximum complexity guarantees at least one of each type
        password = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation)
        ]
        characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the remaining characters, considering the length of the base word
    remaining_length = max(length - len(base_word), 0)
    extra_password = [secrets.choice(characters) for _ in range(remaining_length)]
    password = extra_password + list(base_word)  # Combine the base word with the other generated characters
    
    secrets.SystemRandom().shuffle(password)  # Shuffle the characters so the base word is not obvious
    
    return ''.join(password[:length])  # Ensure the exact length of the password


def display_menu():
    """ 
    Displays the interactive menu for the user to choose the password length, complexity, and base word.
    """
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length for the password (integer): "))
            if length <= 0:
                print("The password length must be greater than zero.")
                continue

            print("Choose the password complexity level:")
            print("1 - Lowercase letters (simpler)")
            print("2 - Uppercase letters, lowercase letters, and numbers (medium)")
            print("3 - Letters, numbers, and special symbols (strong)")
            print("4 - Maximum complexity (includes all characters and guarantees at least one of each type)")
            
            complexity = int(input("Enter the complexity level (1, 2, 3, or 4): "))
            if complexity not in [1, 2, 3, 4]:
                print("Invalid complexity option. Choose 1, 2, 3, or 4.")
                continue
            
            base_word = input("Enter a base word (optional, press Enter to skip): ").strip()
            
            password = generate_password(length, complexity, base_word)
            print(f"\nYour generated password is: {password}\n")
            
            option = input("Do you want to generate another password? (y/n): ").lower()
            if option != 'y':
                print("Closing the password generator. See you next time!")
                break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    display_menu()