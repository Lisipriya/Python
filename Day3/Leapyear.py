# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# The year is multiple of 400.
# The year is multiple of 4 and not multiple of 100.

if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("This is a Leap year.")
    else:
      print("This is not a Leap year.")
  else:
    print("This is a Leap year.")
else:
  print("This is not a Leap year.")