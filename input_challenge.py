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

totalBill = input("How much is your total bill? ")
paymentAmount = input("How much is your payment? ")
change = float(paymentAmount) - float(totalBill)
print("Hi! Your change Php{0} ".format(change))