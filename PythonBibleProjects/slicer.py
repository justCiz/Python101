# get user email address

email = input("What is your email address?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1 :]

# format message

output = "Your username is {0} and your domain name is {1}".format(user, domain)

# display output message 

print(output)
