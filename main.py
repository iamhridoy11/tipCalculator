#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
totalBill = float(input("What was your total bill: $"))

tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15?  "))
numberOfPeople = int(input("How many people to split the bill? "))

splitBill = 0

if tipPercentage == 10:
    splitBill = (totalBill / numberOfPeople) * 1.10
    splitBill = round(splitBill, 2)
    print(f"Each person should pay ${splitBill}")
elif tipPercentage == 12:
    splitBill = (totalBill / numberOfPeople) * 1.12
    splitBill = round(splitBill, 2)
    print(f"Each person should pay ${splitBill}")
elif tipPercentage == 15:
    splitBill = (totalBill / numberOfPeople) * 1.15
    splitBill = round(splitBill, 2)
    print(f"Each person should pay ${splitBill}")
else:
    print("Error")

