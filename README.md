# Password Generator

## Purpose
This project implements a robust password generator capable of creating both **memorable passwords** and **random passwords**. The generator provides flexibility through user interaction or automation and includes features such as saving generated passwords with timestamps to organized directories.

## Features
  **Memorable Password Generator:**
   - Generates passwords using a specified number of random words.
   - Adds a random single-digit number to each word.
   - Concatenates words with hyphens (`-`).
   - Allows customization of the number of words and the case format (lowercase, uppercase, or capitalized).

  **Random Password Generator:**
   - Generates passwords of specified lengths with customizable character types.
   - Includes options to use lowercase letters, uppercase letters, numbers, punctuation symbols, and excluded characters.

  **File Organization:**
   - Saves generated passwords in separate directories (`/Users/lucashandlon/Desktop/I.I. 2/Memorable` and `/Users/lucashandlon/Desktop/I.I. 2/Random`).
   - Each password is saved in a `Generated_Passwords.txt` file with a timestamp.

  **Modes:**
   - **Interactive Mode:** Allows the user to specify settings and generate one password at a time.
   - **Automated Mode:** Automatically generates 1000 passwords, alternating between memorable and random types.

## How to Use

  **Interactive Mode:**
   - Run the script and select the "interactive" mode.
   - Follow prompts to:
     - Choose password type (memorable or random).
     - Configure settings (e.g., number of words for memorable passwords or length for random passwords).
   - The generated password will be displayed in the terminal and saved to the appropriate file.

   **Automated Mode:**
   - Run the script and select the "automated" mode.
   - The script will generate 1000 passwords (500 memorable and 500 random) and save them to the appropriate files automatically.

## Libraries and Modules
The program uses the following Python libraries:
- `os`: For file and directory management.
- `random`: For generating random choices and numbers.
- `string`: For accessing character sets (letters, digits, punctuation).
- `time`: For appending timestamps to passwords.

## Example
### Interactive Mode
```
Choose mode: 'interactive' for manual input or 'automated' to generate 1000 passwords: interactive
Choose password type (memorable/random): memorable
Enter number of words (e.g., 3): 3
Choose word case (lower/upper/capitalize): capitalize
Generated Memorable Password: Lowith9-Ignoramuses6-Chirps2
```

### Automated Mode
```
Choose mode: 'interactive' for manual input or 'automated' to generate 1000 passwords: automated
Generating 1000 passwords randomly between memorable and random
1000 passwords generated and saved.
```

## Directory Structure
```
/Users/lucashandlon/Desktop/I.I. 2/
├── Memorable/
│   └── Generated_Passwords.txt
├── Random/
    └── Generated_Passwords.txt
```

## Notes
- Ensure the word list file (`top_english_nouns_lower_100000.txt`) is available at `/Users/lucashandlon/Desktop/I.I. 2/`.
- Adjust file paths in the script if running on a different system or directory.


