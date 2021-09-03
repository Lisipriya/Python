# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hi "+name+" Good Morning")
  print("Welcome to Python 100 days of coding challenge")
  print("Today's Coding challenge is about functions and inputs\n")

name = input("Enter your name: ")
greet()

#Function with inputs - positional argument
def greet_arg(name, location):
  print(f"Hi {name} Good Morning")
  print(f"How is the weather in {location}\n")

greet_arg("Lisi", "Theni")

#Function with keyword argument
def greet_key(name, location):
  print(f"Hi {name} Good Morning")
  print(f"Whether you are in {location}\n")

greet_key(location ="Theni", name = "Lisi")
greet_key("Theni", "Lisi")