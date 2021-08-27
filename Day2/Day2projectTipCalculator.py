#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to tip calculator.")
Total_Bill = float(input("What was the total bill? "))
Tips = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
Split = int(input("How many people to split the bill? "))
percentage_tip = ((Total_Bill/Split) * (Tips/100))
Bill_split = ((Total_Bill/Split) + percentage_tip)
Amount_per_person = round(Bill_split,2)
print(f"Each person should pay: ₹{Amount_per_person}")