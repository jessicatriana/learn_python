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

# USER INPUT

# name = input("What is your name?")
# age = input("What is your age?")

# print('Hello' + name + '! You are ' + age + ' years old.')

# LISTS

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

# Prints whole list
print(friends)

# Prints 5
print(len(friends))

# Prints 1
print(friends.count('Eric'))

friends.sort()
# Prints the list in A-Z order
print(friends)

friends.sort(reverse=True)
# Prints the list in Z-A order
print(friends)

friends.reverse()
# Prints the list in A-S order because that is reversed from the current state
print(friends)

cars = [911, 130, 328, 535, 740, 308]

# Prints lowest number
print(min(cars))
# Prints highest number
print(max(cars))

# Prints the sum of the numbers
print(sum(cars))

friends.append('TerryG')
# Prints the list with "TerryG" added to the end
print(friends)

friends.insert(1, "Jan")
# Prints the list with "Jan inserted into position 1"
print(friends)

friends[1] = 'TerryG'
# Prints the list with "TerryG" in position 1
print(friends)

friends.extend(cars)
# Prints the "friends" list with the "cars" list added to the end
print(friends)

friends.remove('Terry')
# Prints the list without "Terry"
print(friends)

friends.pop()
# Prints the list without the last name
print(friends)

# del friends
# Deletes the friends list entirely
