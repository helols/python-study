# Day 1
intVal = 5

floatVal = 2.21

boolVal = False

print(boolVal)

boolVal = True

print(intVal)

print(floatVal)

print(boolVal)

# Day 2
"""
This is a multiple line 
comment
"""

add = 3 + 2
sub = 9 - 6
div = 10 / 5
prod = 4 * 7

operators1 = 2
operators2 = 2
operators3 = 2

operators1 **= 2
operators2 //= 0.5
operators3 %= 1

print(add, sub, div, prod)
print(operators1, operators2, operators3)

# Day 3
string = "example"
ex1 = string[0]  # "e"
ex2 = "tape"[2]  # "p"

# Slicing A String

example = "apples"

ex1 = example[:3]  # app 0~N (:excluded)
ex2 = example[2:5]  # ple (included:excluded)
ex3 = example[3:]  #les N~End  (included:)

print(ex1)
print(ex2)
print(ex3)

print('single quotes')
print("double quotes")
print("This should be \"in quotes\".")

gator = "Alligator"
print(gator[5])
print(gator[:4])
print(gator[4:7])
print(gator[6:])

string = "Yoda"
length = len(string)
print(length)  # prints the number of characters in the string "Yoda", which is 4

num = 9
string = str(num)  # turns number 9 to "9" and assigns that string to the variable string
print(string)

str1 = "LOWER"
print(str1.lower())
str2 = "upper"
print(str2.upper())

print(len("Manchester United"))
print(str(12345)[2])
print("albania".upper())
print("BELGIUM".lower())

str1 = "example1"
num = 7
print(str1)
print(num)
print("example2")
print(9)

print("word1" + "word2" + "word3")
print("R" + str(2) + "-D" + str(2))
city = "Seattle"
state = "Washington"

print("The Seahawks are from %s, %s." % (city, state))

occupation = input("What is your occupation?")
city = input("What city do you live in?")
age = input("How many years old are you?")

print("So you are a %s, you live in %s, and you are %s years old." % (occupation, city, age))

name = input("Please enter your name.")
print("Your name is " + "%s" % name)

ex1 = 3 > 1  # True
ex2 = 5 >= 5  # True
ex3 = 3 < 3  # False
ex4 = 7 <= 6  # False
ex5 = 1 == 7  # False
ex6 = 8 != 8  # False

print(8 > 8)
print(6 <= 6)
print(5 < 5)
print(10 != 10)
print(4 == 5)
print(7 >= 7)
print(7 != 9)
print(5 < 9)
print(20 <= 6)
print(5 > 6)
print(20 <= 6)
print(5 > 6)
print(3 == 3)
print(2 >= 1)
