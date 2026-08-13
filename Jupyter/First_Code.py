# ============================================================
# PYTHON BASICS - LEARNING & PRACTICE FILE
# ============================================================
#
# Purpose:
# This file contains beginner Python concepts in a structured
# order with examples and explanations.
#
# Topics Covered:
# 1. print()
# 2. Variables
# 3. Comments
# 4. Naming variables
# 5. Multiple assignment
# 6. Swapping variables
# 7. Local and global variables
# 8. Data types
# 9. Type conversion
# 10. Arithmetic operators
# 11. Strings
# 12. Escape characters
# 13. ord() and chr()
# 14. String indexing and slicing
# 15. String methods
# 16. len()
# 17. startswith() and endswith()
# 18. zfill()
# 19. split() and join()
#
# ============================================================


# ============================================================
# 1. PRINT()
# ============================================================

print("Hello")

# print() is used to display information on the screen.

print("Python is easy to learn")
print(100)
print(10 + 20)


# ============================================================
# 2. VARIABLES
# ============================================================

# A variable is a name used to store a value.

a = 1
b = "DK"

print(a)
print(b)

# Variable values can be changed.

a = 10
a = 20

print(a)


# ============================================================
# 3. VARIABLE NAMING
# ============================================================

# Good variable names should describe the data they contain.

no_of_apple = 5
who_ate = "Switchtech"
roll_number = 1323

print(
    "Apple ate by",
    who_ate,
    "and he ate",
    no_of_apple,
    "number of apples"
)

# Better variable naming:
#
# no_of_apple  -> understandable
# who_ate      -> understandable
# roll_number  -> understandable
#
# Avoid names like:
#
# x = 5
# abc = "Switchtech"
#
# unless they are being used for a very small example.


# IMPORTANT:
# The following is NOT a valid variable assignment:
#
# roll_number1323
#
# Correct:
#
roll_number = 1323


# ============================================================
# 4. F-STRINGS
# ============================================================

customer_id = 123
first_name = "Ram"
last_name = "Prakash"

print(
    f"Customer first name is {first_name}, "
    f"last name is {last_name}, "
    f"and customer ID is {customer_id}"
)

# f-string allows us to insert variables directly inside a string.

# Syntax:
#
# f"some text {variable}"


# ============================================================
# 5. COMMENTS
# ============================================================

# This is a single-line comment.

print("Hello")

# Comments are ignored by Python.
# They are used to explain code.


# Multiline strings:
#
# Triple quotes create a multiline string.
#
# They are NOT technically comments.
#
# They are commonly used for:
# - multiline strings
# - documentation
# - docstrings


"""
This is a multiline string.

It can contain multiple lines.
"""

print("Code execution continues here.")


# ============================================================
# 6. MULTIPLE VARIABLE ASSIGNMENT
# ============================================================

var_1 = 100
var_2 = 200
var_3 = 300

print(var_1)
print(var_2)
print(var_3)

# Python allows multiple assignments in one line.

var_1, var_2, var_3 = 100, 200, 300

print(var_1)
print(var_2)
print(var_3)

# Mapping:
#
# var_1, var_2, var_3 = 100, 200, 300
#    1       2       3     1    2    3


# ============================================================
# 7. ASSIGNING EXISTING VARIABLES
# ============================================================

customer_id = 123
first_name = "Ram"
last_name = "Prakash"

var_4, var_5, var_6 = customer_id, first_name, last_name

print(var_4)
print(var_5)
print(var_6)


# ============================================================
# 8. COPYING VALUES INTO NEW VARIABLES
# ============================================================

test_variable1 = customer_id
test_variable2 = first_name
test_variable3 = last_name

print(test_variable1)
print(test_variable2)
print(test_variable3)


# ============================================================
# 9. SWAPPING VARIABLES
# ============================================================

# Suppose:

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

# Python allows direct swapping.

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# Result:
#
# a = 20
# b = 10


# ============================================================
# 10. LOCAL AND GLOBAL VARIABLES
# ============================================================

# GLOBAL VARIABLE:
# A variable defined outside a function.

global_variable = 100


def example_function():

    # LOCAL VARIABLE:
    # A variable created inside a function.
    local_variable = 200

    print("Inside function:")
    print("Global:", global_variable)
    print("Local:", local_variable)


example_function()

print("Outside function:")
print("Global:", global_variable)

# local_variable cannot normally be accessed outside
# example_function().


# ============================================================
# 11. DATA TYPES
# ============================================================

# Python has several built-in data types.

# int
num = 100
print(num)
print(type(num))

# float
num2 = 10.0
print(num2)
print(type(num2))

# string
name = "Ram"
print(name)
print(type(name))

# complex
complex_number = 10 + 5j
print(complex_number)
print(type(complex_number))

# Common basic data types:
#
# int
# float
# str
# complex
# bool
#
# Later you will learn:
# list
# tuple
# set
# dict


# ============================================================
# 12. ARITHMETIC OPERATORS
# ============================================================

a = 10
b = 20

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", b - a)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", b / a)

# Floor division
print("Floor division:", b // a)

# Modulus / remainder
print("Remainder:", b % a)

# Power
print("Power:", a ** 2)


# ============================================================
# 13. / VS //
# ============================================================

# / = normal division
print(11 / 3)

# // = floor division
print(11 // 3)

# / gives the actual division result.
#
# // gives the floor value.

print(type(11 / 3))
print(type(11 // 3))


# ============================================================
# 14. POWER OPERATOR **
# ============================================================

a = 10
b = 2

print(a ** b)

# 10 ** 2
#
# Means:
#
# 10 * 10
#
# Result:
# 100


# ============================================================
# 15. TYPE CONVERSION
# ============================================================

# Type conversion means changing one data type into another.

# ------------------------------------------------------------
# int -> str
# ------------------------------------------------------------

variable = 10

var2 = str(variable)

print(var2)
print(type(var2))


# ------------------------------------------------------------
# int -> float
# ------------------------------------------------------------

num = 5

print(float(num))


# ------------------------------------------------------------
# float -> int
# ------------------------------------------------------------

num = 10.8

print(int(num))

# NOTE:
# int(10.8) gives 10.
#
# It removes the decimal portion.
# It does not round to the nearest integer.


# ------------------------------------------------------------
# int -> complex
# ------------------------------------------------------------

num = 100

complex_num = complex(num)

print(complex_num)

# Result:
#
# 100 + 0j


# ------------------------------------------------------------
# float -> complex
# ------------------------------------------------------------

num = 10.3

complex_num = complex(num)

print(complex_num)

# Result:
#
# (10.3+0j)


# ============================================================
# 16. STRINGS
# ============================================================

# A string is a sequence of characters.

str1 = "Hello"

str2 = 'Hello'

print(str1)
print(str2)

print(type(str1))


# ============================================================
# 17. SINGLE QUOTES INSIDE STRINGS
# ============================================================

# Problem:
#
# word = 'don't'
#
# Python thinks the string ends at:
# 'don'
#
# Use double quotes instead.

word = "don't"

print(word)


# Or escape the apostrophe:

word = 'don\'t'

print(word)


# ============================================================
# 18. SPECIAL CHARACTERS / ESCAPE SEQUENCES
# ============================================================

# \n = new line

str1 = "We are learning\nData Engineering"

print(str1)


# \t = tab

str2 = "We are learning\tData Engineering"

print(str2)


# ============================================================
# 19. ORD()
# ============================================================

# ord() returns the Unicode number of a character.

print(ord("A"))
print(ord("B"))
print(ord("a"))
print(ord("z"))

# Example:
#
# ord("A") -> 65
# ord("a") -> 97


# ============================================================
# 20. CHR()
# ============================================================

# chr() converts a Unicode number into a character.

print(chr(97))

# Result:
#
# a

print(chr(65))

# Result:
#
# A


# ============================================================
# 21. STRING INDEXING
# ============================================================

text = "engineering"

# Index positions start from 0.

# e n g i n e e r i n g
# 0 1 2 3 4 5 6 7 8 9 10

print(text[0])
print(text[1])
print(text[2])

# First character:
print(text[0])

# Last character:
print(text[-1])


# ============================================================
# 22. STRING SLICING
# ============================================================

text = "engineering"

# Syntax:
#
# string[start:end:step]

# Important:
# The end index is excluded.

print(text[0:4])

# 0 -> e
# 1 -> n
# 2 -> g
# 3 -> i
#
# Result:
# engi


# Start omitted

print(text[:4])


# End omitted

print(text[4:])


# Start and end omitted

print(text[:])


# With step

print(text[0:10:2])


# Reverse string

print(text[::-1])


# ============================================================
# 23. STRING METHODS
# ============================================================

# String methods are functions available for string objects.


# ------------------------------------------------------------
# capitalize()
# ------------------------------------------------------------

str_caps = "hello class"

print(str_caps.capitalize())

# Result:
# Hello class


# ------------------------------------------------------------
# upper()
# ------------------------------------------------------------

str_upper = "hello class"

print(str_upper.upper())


# ------------------------------------------------------------
# lower()
# ------------------------------------------------------------

str_lower = "DJNJDABKJNIJjndsnvonsd"

print(str_lower.lower())


# ------------------------------------------------------------
# title()
# ------------------------------------------------------------

str_title = "data engineering"

print(str_title.title())

# Result:
# Data Engineering


# ------------------------------------------------------------
# swapcase()
# ------------------------------------------------------------

swap = "pyThON"

print(swap.swapcase())

# Result:
# PYtHon


# ------------------------------------------------------------
# replace()
# ------------------------------------------------------------

rep = "class"

print(rep.replace("class", "classroom"))

# Result:
# classroom


# ============================================================
# 24. IMPORTANT CONCEPT:
# STRING METHODS DO NOT MODIFY THE ORIGINAL STRING
# ============================================================

example = "hello"

print(example.upper())

# Original variable is still:
print(example)

# To store the changed value:

example = example.upper()

print(example)


# ============================================================
# 25. count()
# ============================================================

cnt = "where is the classroom"

print(cnt.count("e"))

print(cnt.count("is"))

print(cnt.count(" "))

# count() tells us how many times a substring occurs.


# ============================================================
# 26. len()
# ============================================================

text = "removes leading spaces"

print(len(text))

# len() returns the number of characters.


# ============================================================
# 27. lstrip()
# ============================================================

# Removes spaces from the LEFT side.

ls = "     removes leading spaces   "

print(ls.lstrip())


# ============================================================
# 28. rstrip()
# ============================================================

# Removes spaces from the RIGHT side.

rs = "     removes trailing spaces   "

print(rs.rstrip())


# ============================================================
# 29. strip()
# ============================================================

# Removes spaces from BOTH sides.

text = "     hello python     "

print(text.strip())


# ============================================================
# 30. center()
# ============================================================

text = "Deepak"

print(text.center(14))

# center() places the string in the center
# of the specified width.

print(text.center(14, "*"))

# Example output:
#
# ****Deepak****


# IMPORTANT:
#
# If the requested width is smaller than the string length,
# Python does not shrink the string.

text = "Deepak"

print(text.center(5))


# ============================================================
# 31. startswith()
# ============================================================

exam = "python"

print(exam.startswith("py"))

print(exam.startswith("thon"))


# ============================================================
# 32. endswith()
# ============================================================

exam2 = "python"

print(exam2.endswith("on"))

print(exam2.endswith("py"))


# ============================================================
# 33. zfill()
# ============================================================

# zfill() adds zeros to the LEFT side of a string.

pnr = "2569"

print(pnr.zfill(9))

# Result:
#
# 000002569


# Useful for:
#
# IDs
# Account numbers
# PNR numbers
# Codes
# Fixed-width values


# ============================================================
# 34. SPLIT()
# ============================================================

# split() converts a string into a list.

sentence = "We are learning Python"

words = sentence.split()

print(words)

# Result:
#
# ['We', 'are', 'learning', 'Python']


# split() can also use a specific separator.

data = "apple,banana,orange"

fruits = data.split(",")

print(fruits)


# ============================================================
# 35. JOIN()
# ============================================================

# join() combines list/string elements into one string.

words = ["We", "are", "learning", "Python"]

sentence = " ".join(words)

print(sentence)

# Result:
#
# We are learning Python


# Another example:

fruits = ["apple", "banana", "orange"]

result = ",".join(fruits)

print(result)

# Result:
#
# apple,banana,orange


# ============================================================
# 36. SPLIT + JOIN
# ============================================================

# Very common real-world operation.

text = "Python is easy"

words = text.split()

print(words)

result = "-".join(words)

print(result)

# Result:
#
# Python-is-easy


# ============================================================
# 37. QUICK REFERENCE
# ============================================================

# print()
#   -> Displays information.

# type()
#   -> Returns the data type.

# str()
#   -> Converts value to string.

# int()
#   -> Converts value to integer.

# float()
#   -> Converts value to float.

# complex()
#   -> Converts value to complex number.

# len()
#   -> Returns length.

# ord()
#   -> Character -> Unicode number.

# chr()
#   -> Unicode number -> character.

# capitalize()
#   -> Capitalizes first character.

# upper()
#   -> Converts to uppercase.

# lower()
#   -> Converts to lowercase.

# title()
#   -> Converts words to title case.

# swapcase()
#   -> Swaps uppercase/lowercase.

# replace()
#   -> Replaces part of a string.

# count()
#   -> Counts occurrences.

# lstrip()
#   -> Removes leading whitespace.

# rstrip()
#   -> Removes trailing whitespace.

# strip()
#   -> Removes whitespace from both sides.

# center()
#   -> Centers text within a given width.

# startswith()
#   -> Checks beginning of string.

# endswith()
#   -> Checks ending of string.

# zfill()
#   -> Adds zeros to the left.

# split()
#   -> String -> List.

# join()
#   -> List/String elements -> String.


# ============================================================
# 38. PRACTICE QUESTIONS
# ============================================================

# Practice 1:
# Create variables for:
# customer_id
# customer_name
# customer_city
# customer_age
#
# Print them using an f-string.


# Practice 2:
# Swap:
#
# a = 100
# b = 200
#
# Expected:
#
# a = 200
# b = 100


# Practice 3:
# Convert:
#
# num = 100
#
# into:
# string
# float
# complex


# Practice 4:
# Given:
#
# text = "Data Engineering"
#
# Find:
# - length
# - uppercase
# - lowercase
# - title case
# - first character
# - last character


# Practice 5:
# Given:
#
# text = "Python is easy to learn"
#
# Split the sentence into words.


# Practice 6:
# Given:
#
# words = ["Python", "SQL", "BigQuery"]
#
# Join them using " | ".


# Practice 7:
# Given:
#
# pnr = "2569"
#
# Convert it into:
#
# 000002569


# Practice 8:
# Given:
#
# email = "student@gmail.com"
#
# Check whether the email:
# - starts with "student"
# - ends with ".com"


# ============================================================
# END OF PYTHON BASICS
# ============================================================