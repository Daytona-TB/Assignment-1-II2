# Password Generator

## Purpose
This project implements a password generator capable of creating both **memorable passwords** and **random passwords**. The generator provides flexibility through user interaction or automation and includes features such as saving generated passwords with timestamps to organized directories.

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





