# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(float(weight)/float(height)**2)
#Second method
second_height = float(height)*float(height)
BMI = round(float(weight)/second_height)

print(BMI)

