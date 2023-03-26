# Password Generator Project
# import module
import random

# Declare variable
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

new_random_pass = ""
easy_password = []

len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

# Ask user to insert how many letters, symbols and number would like
print("\nWelcome to the PyPassword Generator!")
nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input(f"How many symbols would you like?\n")
nr_numbers = input(f"How many numbers would you like?\n")


if nr_letters.isnumeric() and (nr_symbols.isnumeric()) and (nr_numbers.isnumeric()):

    nr_letters = int(nr_letters)
    nr_symbols = int(nr_symbols)
    nr_numbers = int(nr_numbers)

    # Check if user choice is greater than dimension of list
    if nr_letters <= len_letters and nr_symbols <= len_numbers and nr_numbers <= len_numbers:

        # "for" cycle to found random letter
        for letter in range(1, nr_letters + 1):
            random_letter = random.randint(0, len_letters - 1)
            easy_password.append(letters[random_letter])

        # "for" cycle to found random numbers
        for number in range(1, nr_numbers + 1):
            random_number = random.randint(0, len_numbers - 1)
            easy_password.append(numbers[random_number])

        # "for" cycle to found random symbols
        for symbol in range(1, nr_symbols + 1):
            random_symbol = random.randint(0, nr_symbols - 1)
            easy_password.append(symbols[random_symbol])

        # Use shuffle() function to mix list
        random.shuffle(easy_password)

        # "for" cycle to write a "new_random_pass"
        for char in easy_password:
            new_random_pass += char

        print(f"Your password is : {new_random_pass}")
    else:
        print("Sorry, your input is grater than dimension of my capacity.")
else:
    print("Sorry, your input is uncorrected. I need tree numbers.")
