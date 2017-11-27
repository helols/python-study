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
ex3 = example[3:]  # les N~End  (included:)

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

# day 4

ex1 = True and True  # True
ex2 = True and False  # false
ex3 = False and False  # False
ex4 = True or True  # True
ex5 = True or False  # True
ex6 = False or False  # False
ex7 = not True  # False
ex8 = not False  # True
ex9 = not False and not True or False
step1 = True and False or False
step2 = False or False
result = False

print(7 > 6 and 6 >= 6)
print(3 != 3 or 4 == 4)
print(not 5 > 2)
print(not 5 < 3 and True or 6 <= 6 and not False)

if 5 != 6:
    print("5 does not equal 6")

if 1 == 2:
    print("1 equals 2.")
else:
    print("1 does not equal 2!")

if 1 == 2:
    print("Don't print this.")
elif 1 != 2:
    print("Print this.")
else:
    print("Don't rint this either.")


if 1 == 2:
    print("Don't print this.")
elif 1 != 1:
    print("Don't print this either.")
elif 5 <= 19:
    print("end elif statement.")
else:
    print("This will not be printed.")

name = input("Enter your name")
nameLen = len(name)
if nameLen < 4:
    print("Your name is less than 4 characters")
elif nameLen < 10:
    print("Your name at least 4 characters and less than 10 characters")
else:
    print("Your name is very long")

# Day 5


def ex():
    print("Hello world")


ex()


def single(a):
    print(a)


single(9)


def mult(a, b, c):
    d = a * b
    print(d+c)


mult(2, 3, 4)


def giver(a, b):
    c = a + b
    return c


def taker(d, e):
    output = giver(d, e)
    return output


print(taker(1, 5))


def first():
    print("This is a function")


def intFun(intVal):
    return intVal * 2


def takesTwo(int1, int2):
    return int1 * int2

def functionInside(a, b, c):
    print(takesTwo(intFun(a), b) * c)


first()

functionInside(7, 4, 2)
