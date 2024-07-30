# Print
print("Hello, World!")

# Python escape and newline characters
print("Hello\nWorld!")

# Using multiple arguments
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

# Keyword arguments
# The default behavior reflects the situation where the end keyword argument is implicitly used in the following way: end="\n".
print("My name is", "Python.", end=" ")
print("My", "name", "is", "Monty", "Python.", sep="-")

print("My", "name", "is", sep="_", end="*")
print("Francis")

print('"Greg\'s book."')

# Replication
# The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


# Using .format() function to attach a string
name = "Francis"
print('Hello {}'.format(name))
print('Hello {0}'.format(name))