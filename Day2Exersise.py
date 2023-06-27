# Day 2 exercise

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 20 or 15? "))
people = int(input("How many people to split the bill? "))
bill_percentage = (percentage/100)*bill
total_bill = bill_percentage + bill
bill_per_person = total_bill / people
print("Each person should pay: ", round(bill_per_person,2))