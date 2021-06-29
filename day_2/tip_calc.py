#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print(">> Welcome to the tip calculator <<")

bill_amt = int(input("Enter the amount of bill: \n"))
perc_tip = int(input("What percentage of tip would you like to give? "))
no_ppl = int(input("How many people to split the bill? \n"))

total_bill = bill_amt * (1+(perc_tip/100))
total_bill_pp = round(total_bill/no_ppl, 2)
total_bill_pp = "{:.2f}".format(total_bill_pp)

print(f"Each person should pay : ${total_bill_pp}\n")
