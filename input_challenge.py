""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

"""
totalBill = input("Enter Total Bill: ")
paymentAmount = input("Enter Payment Amount: ")
change = totalBill - paymentAmount
print("Total bill: {0}\n Payment Amount: {1}\n Your change is Php{2}".format(totalBill, paymentAmount, change))
"""

while(True):
	try:
		totalBill = float(input("How much is your total bill? "))
		break
	except Exception as e:
		print("Invalid input. Please enter a number.")

while(True):
	try:
		paymentAmount = float(input("How much is your payment? "))
		break
	except Exception as e:
		print("Invalid input. Please enter a number.")


change = paymentAmount - totalBill
print("Hi! Your change Php {0:.2f}".format(change))