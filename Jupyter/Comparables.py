# ============================================================
# PYTHON BASICS - CONDITIONAL STATEMENTS
# ============================================================
#
# Topics Covered:
#
# 1. if statement
# 2. else statement
# 3. if-else
# 4. elif
# 5. Comparison operators
# 6. Logical operators
# 7. Checking string membership using "in"
# 8. input()
# 9. Converting input using int()
# 10. Nested if
# 11. Multiple conditions
# 12. Practical examples
#
# ============================================================


# ============================================================
# 1. IF STATEMENT
# ============================================================

# The if statement is used to execute a block of code
# when a condition is True.

# Syntax:
#
# if condition:
#     statement


a = 33
b = 45

if a > b:
    print("a is greater than b")


# In this example:
#
# a > b
#
# becomes:
#
# 33 > 45
#
# This is False.
#
# Therefore, the print statement is NOT executed.


# ============================================================
# 2. IF-ELSE STATEMENT
# ============================================================

# if:
#     Executes when condition is True.
#
# else:
#     Executes when condition is False.


a = 33
b = 45

if a > b:
    print("addition of {} and {} is {}".format(a, b, a + b))
else:
    print("multiplication of {} and {} is {}".format(a, b, a * b))


# Since:
#
# 33 > 45
#
# is False,
# the else block will execute.


# ============================================================
# 3. ANOTHER IF-ELSE EXAMPLE
# ============================================================

a = 63
b = 45

if a > b:
    print("addition of {} and {} is {}".format(a, b, a + b))
else:
    print("multiplication of {} and {} is {}".format(a, b, a * b))


# Here:
#
# 63 > 45
#
# is True.
#
# Therefore, the if block executes.


# ============================================================
# 4. .format() METHOD
# ============================================================

a = 10
b = 20

print(
    "The values are {} and {}. Their addition is {}".format(
        a,
        b,
        a + b
    )
)


# {} acts as a placeholder.
#
# .format(a, b, a + b)
#
# fills the placeholders from left to right.


# ============================================================
# 5. SAME EXAMPLE USING F-STRING
# ============================================================

a = 10
b = 20

print(f"The values are {a} and {b}. Their addition is {a + b}")


# f-string is generally easier to read.


# ============================================================
# 6. ELIF
# ============================================================

# elif means:
#
# "else if"
#
# It is used when we have multiple conditions.


# Syntax:
#
# if condition1:
#     statement
#
# elif condition2:
#     statement
#
# elif condition3:
#     statement
#
# else:
#     statement


# ============================================================
# 7. FIND THE GREATEST OF THREE NUMBERS
# ============================================================

x = 10
y = 20
z = 30

if x > y and x > z:
    print("x is highest")

elif y > x and y > z:
    print("y is highest")

elif z > x and z > y:
    print("z is highest")

else:
    print("Some values are equal")


# Here:
#
# x > y
# and
# x > z
#
# means x must be greater than BOTH y and z.


# ============================================================
# 8. BETTER VERSION - FIND MAXIMUM
# ============================================================

x = 10
y = 20
z = 30

if x >= y and x >= z:
    print("x is highest")

elif y >= x and y >= z:
    print("y is highest")

else:
    print("z is highest")


# This version handles equal values more naturally.
#
# However, if you specifically need to identify:
#
# - all three equal
# - two equal
# - one highest
#
# then use the following version.


# ============================================================
# 9. HANDLING EQUAL VALUES
# ============================================================

x = 10
y = 20
z = 30

if x == y and y == z:
    print("All three values are equal")

elif x >= y and x >= z:
    print("x is highest")

elif y >= x and y >= z:
    print("y is highest")

else:
    print("z is highest")


# ============================================================
# 10. COMPARISON OPERATORS
# ============================================================

# Comparison operators return True or False.

a = 10
b = 20

print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to


# ============================================================
# 11. LOGICAL OPERATORS
# ============================================================

# Python has three major logical operators:
#
# and
# or
# not


# ------------------------------------------------------------
# AND
# ------------------------------------------------------------

# Both conditions must be True.

age = 25

if age >= 18 and age <= 60:
    print("Age is between 18 and 60")


# ------------------------------------------------------------
# OR
# ------------------------------------------------------------

# At least one condition must be True.

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# ------------------------------------------------------------
# NOT
# ------------------------------------------------------------

# not reverses True/False.

is_raining = False

if not is_raining:
    print("It is not raining")


# ============================================================
# 12. MEMBERSHIP OPERATOR - IN
# ============================================================

# "in" checks whether a value exists inside a sequence.


test_str = "python and data engineering"

if "python" in test_str:
    print("python is present")
else:
    print("python is not present")


# Another example:

if "abcde" in test_str:
    print("abcde is present")
else:
    print("abcde is not present")


# Since "abcde" does not exist in test_str,
# the else block executes.


# ============================================================
# 13. NOT IN
# ============================================================

test_str = "python and data engineering"

if "java" not in test_str:
    print("java is not present")


# ============================================================
# 14. CASE SENSITIVITY
# ============================================================

text = "Python"

print("Python" in text)
print("python" in text)


# Output:
#
# True
# False
#
# Python string comparisons are case-sensitive.


# ============================================================
# 15. INPUT()
# ============================================================

# input() is used to accept information from the user.


name = input("Enter your name: ")

print("Hello", name)


# IMPORTANT:
#
# input() returns a STRING.
#
# Example:
#
# a = input()
#
# If user enters:
#
# 33
#
# Python stores:
#
# "33"
#
# NOT:
#
# 33


# ============================================================
# 16. INPUT() AND COMPARISON
# ============================================================

a = input("Enter value for a: ")
b = input("Enter value for b: ")

print(type(a))
print(type(b))


# Both a and b are strings.


# ============================================================
# 17. WHY int(input()) IS IMPORTANT
# ============================================================

# If we want numerical calculations,
# convert input to int.


a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

if a > b:
    print("addition of {} and {} is {}".format(a, b, a + b))
else:
    print("multiplication of {} and {} is {}".format(a, b, a * b))


# Now:
#
# a and b are integers.
#
# Therefore:
#
# a + b
# a * b
# a > b
#
# all work numerically.


# ============================================================
# 18. STRING INPUT VS INTEGER INPUT
# ============================================================

# STRING INPUT
#
# a = input()
#
# returns:
# str


# INTEGER INPUT
#
# a = int(input())
#
# returns:
# int


# FLOAT INPUT
#
# a = float(input())
#
# returns:
# float


# ============================================================
# 19. NESTED IF
# ============================================================

# An if statement inside another if statement
# is called a nested if.


score = int(input("Enter the score: "))

if score >= 50:

    if score >= 75:

        if score >= 90:
            print("Grade A")

        else:
            print("Grade B")

    else:
        print("Grade C")

else:
    print("Fail")


# Logic:
#
# score < 50
#     -> Fail
#
# score >= 50 and < 75
#     -> Grade C
#
# score >= 75 and < 90
#     -> Grade B
#
# score >= 90
#     -> Grade A


# ============================================================
# 20. SAME GRADING LOGIC USING ELIF
# ============================================================

score = int(input("Enter the score: "))

if score >= 90:
    print("Grade A")

elif score >= 75:
    print("Grade B")

elif score >= 50:
    print("Grade C")

else:
    print("Fail")


# This is simpler than nested if for this particular problem.


# ============================================================
# 21. IMPORTANT:
# ORDER OF CONDITIONS MATTERS
# ============================================================

score = 95

if score >= 50:
    print("Pass")

elif score >= 90:
    print("Grade A")


# This will print:
#
# Pass
#
# Why?
#
# Because 95 >= 50 is already True.
#
# Python does not continue checking the elif.
#
# Therefore, when using elif, put the more specific/highest
# conditions first.


# Correct:

score = 95

if score >= 90:
    print("Grade A")

elif score >= 75:
    print("Grade B")

elif score >= 50:
    print("Grade C")

else:
    print("Fail")


# ============================================================
# 22. IF / ELIF / ELSE FLOW
# ============================================================

# Python checks conditions from TOP to BOTTOM.
#
# Example:
#
# if condition1:
#     execute
#
# elif condition2:
#     execute
#
# elif condition3:
#     execute
#
# else:
#     execute
#
#
# Only the FIRST True condition is executed.


# ============================================================
# 23. SIMPLE AGE EXAMPLE
# ============================================================

age = int(input("Enter your age: "))

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior")


# ============================================================
# 24. POSITIVE / NEGATIVE / ZERO
# ============================================================

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")


# ============================================================
# 25. EVEN / ODD
# ============================================================

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")

else:
    print("Odd number")


# % gives the remainder.
#
# Example:
#
# 10 % 2 = 0
# 11 % 2 = 1


# ============================================================
# 26. CHECK WHETHER NUMBER IS BETWEEN TWO VALUES
# ============================================================

number = int(input("Enter a number: "))

if number >= 10 and number <= 50:
    print("Number is between 10 and 50")

else:
    print("Number is outside the range")


# Python also allows:

if 10 <= number <= 50:
    print("Number is between 10 and 50")


# ============================================================
# 27. CHECK LOGIN CREDENTIALS
# ============================================================

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")

else:
    print("Invalid username or password")


# ============================================================
# 28. PRACTICAL EXAMPLE - DISCOUNT
# ============================================================

amount = float(input("Enter purchase amount: "))

if amount >= 10000:
    discount = amount * 0.20

elif amount >= 5000:
    discount = amount * 0.10

elif amount >= 2000:
    discount = amount * 0.05

else:
    discount = 0


final_amount = amount - discount

print("Original amount:", amount)
print("Discount:", discount)
print("Final amount:", final_amount)


# ============================================================
# 29. IMPORTANT DIFFERENCE:
# IF vs IF-ELIF
# ============================================================

# Multiple independent IF statements:

score = 95

if score >= 50:
    print("Pass")

if score >= 75:
    print("Good score")

if score >= 90:
    print("Excellent score")


# All three conditions are checked.


# ------------------------------------------------------------
# IF-ELIF
# ------------------------------------------------------------

score = 95

if score >= 90:
    print("Grade A")

elif score >= 75:
    print("Grade B")

elif score >= 50:
    print("Grade C")

else:
    print("Fail")


# Only one block executes.


# ============================================================
# 30. YOUR ORIGINAL "code" EXAMPLE - CORRECTED
# ============================================================

score = int(input("Enter the score: "))

if score >= 50:
    print("Pass")

else:
    print("Fail")


# The original:
#
# if score >= 50:
#     code
#
# is not a complete useful statement.
#
# If "code" has not been defined as a variable or function,
# Python will raise:
#
# NameError


# ============================================================
# 31. BASIC CONDITIONAL STATEMENT TEMPLATE
# ============================================================

# if condition:
#     statement
#
# elif another_condition:
#     statement
#
# else:
#     statement


# ============================================================
# 32. CONDITIONAL OPERATORS QUICK REFERENCE
# ============================================================

# ==     Equal to
# !=     Not equal to
# >      Greater than
# <      Less than
# >=     Greater than or equal to
# <=     Less than or equal to
#
# and    Both conditions must be True
# or     At least one condition must be True
# not    Reverses the condition
# in     Checks membership
# not in Checks absence


# ============================================================
# 33. PRACTICE QUESTIONS
# ============================================================

# Practice 1:
#
# Take two numbers from the user.
# Print which number is greater.


# Practice 2:
#
# Take three numbers from the user.
# Find the greatest number.


# Practice 3:
#
# Take a number from the user.
# Check whether it is:
# - Positive
# - Negative
# - Zero


# Practice 4:
#
# Take a number from the user.
# Check whether it is even or odd.


# Practice 5:
#
# Take marks from the user.
#
# 90 or above -> Grade A
# 75-89       -> Grade B
# 50-74       -> Grade C
# Below 50    -> Fail


# Practice 6:
#
# Take age from the user.
#
# Below 13 -> Child
# 13-19    -> Teenager
# 20-59    -> Adult
# 60+      -> Senior


# Practice 7:
#
# Take a string from the user.
# Check whether "python" exists in the string.


# Practice 8:
#
# Take username and password from the user.
# Check whether they match the expected values.


# Practice 9:
#
# Take purchase amount from the user.
#
# >= 10000 -> 20% discount
# >= 5000  -> 10% discount
# >= 2000  -> 5% discount
# Otherwise -> No discount


# Practice 10:
#
# Take a year from the user.
# Check whether it is a leap year.


# ============================================================
# END OF CONDITIONAL STATEMENTS
# ============================================================