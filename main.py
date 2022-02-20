# Day 5 Password Generator Project (final)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

total_string = " "

for letters_ in range(0,nr_letters):
  random_letters = random.choice(letters)
  total_string += random_letters

for numbers_ in range(0,nr_numbers):
  random_number = random.choice(numbers)
  total_string += random_number

for symbols_ in range(0,nr_symbols):
  random_symbols = random.choice(symbols)
  total_string += random_symbols

print(f"Your Pass Word is : {total_string}")

# #Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P3

total_list = []

for letters_ in range(0,nr_letters):
  random_letters = random.choice(letters)
  total_list += random_letters

for numbers_ in range(0,nr_numbers):
  random_number = random.choice(numbers)
  total_list += random_number

for symbols_ in range(0,nr_symbols):
  random_symbols = random.choice(symbols)
  total_list += random_symbols

total_string_1 = " "
random.shuffle(total_list)
for i in total_list:
  total_string_1 += i
print(total_string_1)
