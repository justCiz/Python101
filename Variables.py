# Variable
#     the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
#     the name of the variable must begin with a letter;
#     the underscore character is a letter;
#     upper- and lower-case letters are treated as different (a little differently than in the real world – Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
#     the name of the variable must not be any of Python's reserved words (the keywords – we'll explain more about this soon).

# Note that the same restrictions apply to function names.

# Python does not impose restrictions on the length of variable names, but that doesn't mean that a long variable name is always better than a short one.


# just use the name of the desired variable, then the equal sign (=) and the value you want to put into the variable.
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

a,b,c = 1,2,3
print(a)
print(b)
print(c)

# Input
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
