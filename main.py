import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

combination = []


print("Welcome to the Magnificent Python Password Generator!")

num_of_letter = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))
num_of_numbers = int(input("How many numbers would you like in your password?\n"))

for i in range(num_of_letter):
    combination.append(random.choice(letters))

for i in range(num_of_symbols):
    combination.append(random.choice(symbols))

for i in range(num_of_numbers):
    combination.append(random.choice(numbers))



random.shuffle(combination)
combination = "".join(map(str, combination))

print(f"Password generated! You used {num_of_letter} letters, {num_of_symbols} symbols and {num_of_numbers} numbers!")
print(f"Enjoy your new pasword: {combination}")