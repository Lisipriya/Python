# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_name1 = name1.lower().replace(' ', '')
lowercase_name2 = name2.lower().replace(' ', '')
name_combine = lowercase_name1 + lowercase_name2

true = str(name_combine.count('t') + name_combine.count('r') + name_combine.count('u') + name_combine.count ('e'))

love = str(name_combine.count('l') + name_combine.count('o') + name_combine.count('v') + name_combine.count ('e'))

love_cal_val = true + love
Love_Calculator = int(love_cal_val)

if (Love_Calculator<10) or (Love_Calculator>90):
  print(f"Your score is {Love_Calculator}, you go together like coke and mentos.")

elif (Love_Calculator>= 40) and (Love_Calculator <=50):
  print(f"Your score is {Love_Calculator}, you are alright together.")

else:
  print(f"Your score is {Love_Calculator}")
