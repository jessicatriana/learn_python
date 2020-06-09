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

# STRING PRACTICE

msg = 'welcome to Python 101: Strings'
# Goal is to print "1 Welcome Ring To Tyler"
msg1 = msg[18] + ' ' + msg[:8]+msg[25:29] + msg[7:11] + \
    msg[13] + msg[12] + msg[2] + msg[1] + msg[-5]
print(msg1.title())

# Prints the message backwards
print(msg1[::-1].title())

# Tripel quotes print a multiline string
msg = """This is a 
multiline
string."""

print(msg)

msg = 'Welcome to Python 101: Strings'
# Prints 11 since it starts at position 11
print(msg.find("Python"))

# Prints "Welcome to Java 101: Strings" using find and replace
print(msg.replace('Python', 'Java'))

# Prints "Welcome to C 101: Strings" but this time stored in a variable
new_msg = msg.replace('Python', 'C')
print(new_msg)

# Prints false - checks to see if "Python" is in new_message
print('Python' in new_msg)

# String formatting

name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
# Prints [TERRY] loves the color red!
print(msg)
