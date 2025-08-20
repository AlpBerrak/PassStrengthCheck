# PassStrengthCheck
## About:
A Python script to evaluate the strength of a password. It checks for character variety, estimates entropy, and provides an approximate crack time, helping users create more secure passwords.

## Features:
- Checks for presence of:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Symbols (25 allowed special characters)
- Estimates password entropy (in bits)
- Estimates crack time assuming 1 billion guesses per second
- Provides an overall strength rating: Very Weak, Weak, Reasonable, Strong, Very Strong
- Simple and easy-to-read output

## Installation:
1. Clone the Repo
- ```git clone https://github.com/AlpBerrak/PassStrengthCheck.git```
2. Navigate to the repo
3. Run the file
- ```python StrengthCheck.py```

## Features to be added:
- Password improvement suggestions
  - options to:
    - randomize caps
    - change letters into numbers and symbols