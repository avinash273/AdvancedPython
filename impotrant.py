"""
Read this before interview, will make coding easier
Also, read online about the time complexity of these inbuilt functions
"""
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven"]

# File operations
with open("testfile.txt", "r") as fp:
    for line in iter(fp.readline, ''):
        print(line)

# use regular interaction over the days
for m in range(len(days)):
    print(m + 1, days[m])

# using enumerate reduces code and provides a counter
for i, m in enumerate(days, start=1):
    print(i, m)

# use zip to combine sequences
for m in zip(days, daysFr):
    print(m)

for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], "=", m[1], "in French")

nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"
grades = (81, 89, 94, 78, 61, 66, 99, 74)


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def squareFunc(x):
    return x ** 2


# use filter to remove items from a list
odds = list(filter(filterFunc, nums))
print(odds)

# use filter on non-numeric sequence
lowers = list(filter(filterFunc2, chars))
print(lowers)

# use map to create a new sequence of values
squares = list(map(squareFunc, nums))
print(squares)

# For initializing lowest value
import sys

n = -sys.maxsize - 1


# the power
def power(x):
    return x ** 3


# define a function that takes variable arguments
def addition(base, *args):
    result = 0
    for arg in args:
        result += arg
    return result


# Use lambdas to accomplish small func like Cel to Far
ftemps = [32, 65, 100, 212]
print(list(map(lambda t: (t - 32) * 5 / 9, ftemps)))

# Used to get alphabet strings (abcde.. ABCD.. abcde.ABCDEF)
import string
a = string.ascii_lowercase
A = string.ascii_uppercase
num = string.ascii_letters
print(a, A, num)
# convert to upper, works for whole string as well
print(a[1].upper())

# reverse a string
ftemps = [32, 65, 100, 212]
print(ftemps[::-1])

# raise error
if (1 == 2):
    print(1)
else:
    raise ArithmeticError("check")