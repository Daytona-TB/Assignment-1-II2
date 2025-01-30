import os
import random
import string
import time

class PasswordGenerator:
    def __init__(self, exclude_chars=""):
        """Base class for password generators."""
        self.exclude_chars = exclude_chars

    def save_password(self, password, password_type):
        """Save the generated password to a file."""
        directory = "/Users/lucashandlon/Desktop/I.I. 2"
        file_path = os.path.join(directory, password_type, "Generated_Passwords.txt")

        if not os.path.exists(os.path.join(directory, password_type)):
            os.makedirs(os.path.join(directory, password_type))

        with open(file_path, "a") as file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {password}\n")

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length=12, include_lowercase=True, include_uppercase=True, 
                 include_numbers=True, include_punctuation=True, exclude_chars=""):
        super().__init__(exclude_chars)
        self.length = length
        self.include_lowercase = include_lowercase
        self.include_uppercase = include_uppercase
        self.include_numbers = include_numbers
        self.include_punctuation = include_punctuation

    def generate(self):
        """Generate a random password based on specified criteria."""
        char_set = ""
        if self.include_lowercase:
            char_set += string.ascii_lowercase
        if self.include_uppercase:
            char_set += string.ascii_uppercase
        if self.include_numbers:
            char_set += string.digits
        if self.include_punctuation:
            char_set += string.punctuation
        
        char_set = ''.join(c for c in char_set if c not in self.exclude_chars)
        if not char_set:
            raise ValueError("No valid characters available to generate the password.")
        
        return ''.join(random.choice(char_set) for _ in range(self.length))

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_words=3, case="lower", word_list_file=""):
        super().__init__()
        self.num_words = num_words
        self.case = case
        self.word_list_file = word_list_file

    def generate(self):
        """Generate a memorable password using words from a file."""
        if not self.word_list_file:
            raise ValueError("Word list file path is not set.")
        
        try:
            with open(self.word_list_file, "r") as file:
                words = [line.strip() for line in file]
        except FileNotFoundError:
            raise FileNotFoundError(f"Word list file '{self.word_list_file}' not found.")
        
        selected_words = random.sample(words, self.num_words)

        if self.case == "upper":
            selected_words = [word.upper() for word in selected_words]
        elif self.case == "capitalize":
            selected_words = [word.capitalize() for word in selected_words]

        return "-".join(f"{word}{random.randint(0, 9)}" for word in selected_words)

if __name__ == "__main__":
    mode = input("Choose mode: 'interactive' for manual input or 'automated' to generate 1000 passwords: ").strip().lower()

    if mode == "interactive":
        password_type = input("Choose password type (memorable/random): ").strip().lower()

        if password_type == "memorable":
            try:
                num_words = int(input("Enter number of words (e.g., 3): "))
                case = input("Choose word case (lower/upper/capitalize): ").strip().lower()
                word_list_file = "/Users/lucashandlon/Desktop/I.I. 2/top_english_nouns_lower_100000.txt"

                generator = MemorablePasswordGenerator(num_words=num_words, case=case, word_list_file=word_list_file)
                password = generator.generate()
                print(f"Generated Memorable Password: {password}")
                generator.save_password(password, "Memorable")
            except Exception as e:
                print(f"Error: {e}")

        elif password_type == "random":
            try:
                length = int(input("Enter password length (e.g., 12): "))
                include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == "yes"
                include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
                include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
                include_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == "yes"
                exclude_chars = input("Enter characters to exclude (leave blank for none): ").strip()

                generator = RandomPasswordGenerator(length, include_lowercase, include_uppercase, include_numbers, include_punctuation, exclude_chars)
                password = generator.generate()
                print(f"Generated Random Password: {password}")
                generator.save_password(password, "Random")
            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Invalid password type. Please choose 'memorable' or 'random'.")

    elif mode == "automated":
        print("Generating 1000 passwords randomly between memorable and random")
        word_list_file = "/Users/lucashandlon/Desktop/I.I. 2/top_english_nouns_lower_100000.txt"

        for _ in range(1000):
            password_type = random.choice(["memorable", "random"])

            if password_type == "memorable":
                try:
                    generator = MemorablePasswordGenerator(num_words=3, case="lower", word_list_file=word_list_file)
                    password = generator.generate()
                    generator.save_password(password, "Memorable")
                except Exception as e:
                    print(f"Error generating memorable password: {e}")

            elif password_type == "random":
                try:
                    generator = RandomPasswordGenerator(
                        length=12, include_lowercase=True, include_uppercase=True, 
                        include_numbers=True, include_punctuation=True
                    )
                    password = generator.generate()
                    generator.save_password(password, "Random")
                except Exception as e:
                    print(f"Error generating random password: {e}")

        print("1000 passwords generated and saved.")

    else:
        print("Invalid mode. Please choose 'interactive' or 'automated'.")
