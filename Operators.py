# Operators in python
# + = addition
# - = subtraction
# * = multiplication
# / = division
# // = floor division
# % = modulus
# ** = exponentiation           

# Remember on * and **:
#     when both arguments are integers, the result is an integer, too;
#     when at least one argument is a float, the result is a float, too.
print("2 * 3 = ", 2 * 3)
print("2 * 3. = ", 2 * 3.)
print("2. * 3 = ", 2. * 3)
print("2. * 3. = ", 2. * 3.)

# The result produced by the division operator is always a float.
print("6 / 3 = ", 6 / 3)
print("6 / 3. = ", 6 / 3.)
print("6. / 3 = ", 6. / 3)
print("6. / 3. = ", 6. / 3.)

# A // (double slash) sign is an integer division operator. It differs from the standard / operator in two details:
#     results are always rounded
print("6 // 3 = ", 6 // 3)
print("6 // 3. = ", 6 // 3.)
print("6. // 3 = ", 6. // 3)
print("6. // 3. = ", 6. // 3.)

# Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.
print("9 % 6 % 2 = ", 9 % 6 % 2)
print("2 ** 2 ** 3 = ", 2 ** 2 ** 3)

# Logical Operators
# and, or, not
print("not True = ", not True)
print("not False = ", not False)
print("True and False = ", True and False)
print("True or False = ", True or False)

3# Nested If
x = 10
 
if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")


# While
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# For
for i in range(10):
    print("[for i in range(10)] The value of i is currently", i)

# the first argument determines the initial (first) value of the control variable
# the second argument determines the boundary (the value which is not allowed to be reached)
for i in range(2, 8):
    print("[for i in range(2, 8)] The value of i is currently", i)

# the third argument is optional, and if it's used, it must be an integer; 
# it determines the increment by which the control variable will be increased
for i in range(2, 8, 3):
    print("[for i in range(2, 8, 3)] The value of i is currently", i)

# break – exits the loop immediately, and unconditionally ends the loop's operation
# continue – behaves as if the program has suddenly reached the end of the body

