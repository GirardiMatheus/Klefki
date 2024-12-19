# Klefki - Secure Password Generator

Klefki is a highly secure and customizable password generator written in Python. It allows users to generate strong passwords with varying levels of complexity and even integrate a custom **base word** into the password. Klefki is designed to ensure the security and unpredictability of the generated passwords.

## Features
- **Customizable Complexity**: Choose from 4 levels of complexity:
  - **Level 1**: Lowercase letters only.
  - **Level 2**: Uppercase, lowercase letters, and numbers.
  - **Level 3**: Letters, numbers, and special characters.
  - **Level 4**: Maximum complexity, guaranteeing at least one lowercase, one uppercase, one number, and one special character.
- **Custom Base Word**: Optionally, you can provide a base word that will be embedded into the password.
- **Randomized Character Shuffling**: Characters are randomly shuffled to prevent predictability of the base word's location.
- **Security**: Uses Python's `secrets` module to ensure strong, cryptographically secure randomization.

## How It Works
1. The user inputs the desired password length.
2. The user selects a complexity level (1 to 4).
3. The user can optionally provide a base word to be embedded in the password.
4. Klefki generates a password based on the user's input, ensuring it meets the specified complexity requirements.

## Usage
To run Klefki, simply execute the following command in your terminal:

```bash
python3 main.py
```

### Example Usage
```
Welcome to the Password Generator!
Enter the desired length for the password (integer): 12
Choose the password complexity level:
1 - Lowercase letters (simpler)
2 - Uppercase letters, lowercase letters, and numbers (medium)
3 - Letters, numbers, and special symbols (strong)
4 - Maximum complexity (includes all characters and guarantees at least one of each type)
Enter the complexity level (1, 2, 3, or 4): 3
Enter a base word (optional, press Enter to skip): secure

Your generated password is: a9$ecurelP!#
```

## Code Overview
The main file consists of the following key functions:

- **`generate_password(length: int, complexity: int, base_word: str = "")`**:
  - Generates a secure password based on the specified length, complexity, and optional base word.
  - Uses cryptographically secure randomization from the `secrets` module.

- **`display_menu()`**:
  - Interactive menu for users to select password length, complexity, and base word.
  - Handles user input and guides users through the process.

## Installation
No special libraries are required, as it uses Python's standard library. To run Klefki, you need:
- **Python 3.6+** installed on your system.

## Security Notes
Klefki prioritizes password security by leveraging Python's `secrets` module, which is specifically designed for cryptographic security. The password is randomized, and the use of a **base word** does not compromise its unpredictability thanks to character shuffling.

## Possible Improvements
- Add a graphical user interface (GUI) using `tkinter`.
- Add command-line arguments to allow non-interactive usage.
- Include more advanced password strength analysis and feedback.

## Contributing
Contributions are welcome! If you'd like to add features or fix issues, feel free to open a pull request.

## License
This project is open-source and licensed under the **MIT License**.
