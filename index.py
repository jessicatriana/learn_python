# VARIABLES AND DATATYPES

print('Variables & Datatypes - Exercise')

item_name = 'widget'
price = 23.50
inventory = 100
is_in_inventory = True

print(item_name, price, inventory)

# BASIC ARITHMETIC

print("Basic Arithmetic")

a = 12
b = 5
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

# STRING BASICS

msg = 'Welcome to Python 101'
# Prints without a space
print(msg*2)

# Prints with a space
print(msg, msg)
# Prints all uppercase
print(msg.upper())
# Prints all lowercase
print(msg.lower())
# Prints with first letter of first word capitalized, all others lowercase
print(msg.capitalize())
# Prints all words with first letter capitalized
print(msg.title())
# Prints 21
print(len(msg))
# Prints 2
print(msg.count('t'))
# Prints m
print(msg[5])
# Prints 1
print(msg[-1])
# Prints lcome to Python 101 (everything after the 2nd position)
print(msg[2:])
# Prints lcome (everything between the 2nd and 7th positions)
print(msg[2:7])