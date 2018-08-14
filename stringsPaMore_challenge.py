""" Aling Nena's Reward System Challenge
Author:
Description: This summer, Aling Nena’s Sari-sari store wants to implement a
reward system where customers can redeem a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>

>> Please enter text: 1 nicole i. tibay f

The system will then reply the following:
Hi <Customer’s name first letters upper case>! You have successfully redeem
reward #<reward number> - <reward>! Thank you for choosing Aling Nena’s
Sari-sari store.

>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank you for choosing Aling Nena’s Sari-sari store.
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
rewards = [
    "Coke sakto",  # index 0
    "Boy Bawang",  # index 1
    "15pcs. Yucky candy",  # index 2
    "15pcs. Pintura candy",  # index 3
    "15PHP load",  # index 4
    "3 pcs. Dove conditioner",  # index 5
    "Cottonbuds",  # index 6
    "One sheet of Biogesic",  # index 7
    "100mL Pepper/Pintura",  # index 8
]

print("Please enter your information in ff format: <Reward number 1-9> <Customer’s name> <Gender f or m>")
while(True):
	try:
		custDetails = (input("Please enter text: ")).split()

		hasError = False

		rewardID = int(custDetails[0])
		if(rewardID > 0 and rewardID < 10):
			rewardDesc = rewards[rewardID - 1]
			del custDetails[0]
		else:
			print("Invalid reward number. Reward number must be from 1 - 9 only.")
			hasError = True

		gender = custDetails[len(custDetails) - 1].upper()
		if(gender == "F" or gender == "M"):
			namePrefix = ("Ma'am" if gender == "F" else "Sir")
			del custDetails[len(custDetails) - 1]
		else:
			print("Invalid input. Please input 'M' if Male and 'F' if Female.")
			hasError = True

		if(len(custDetails) > 0):
			custName = (' '.join(custDetails)).title()
		else:
			print("Invalid customer name. Please input your name to claim your reward.")
			hasError = True

		if(hasError == False):
			print("Hi {0} {1}!".format(namePrefix, custName))
			print("You have successfully redeem reward #{0} - {1}!".format(rewardID, rewardDesc))
			print("Thank you for choosing Aling Nena’s Sari-sari store.")

		break
	except Exception as e:
		print("Invalid input. Please follow the format given.")
