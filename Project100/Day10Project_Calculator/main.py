from replit import clear
import art
#Calculator
#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#modulo
def modulo(n1, n2):
  return n1 % n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
  "%" : modulo
}



def calculator():
  print(art.logo)
  def result(n1, n2):
    function = operations[operation_symbol]
    num_1 = function(n1, n2)
    return num_1

  num_1 = float(input("Enter the first number: "))
  for symbol in operations:
    print(symbol)

  continue_calculation = True

  while continue_calculation:  
    operation_symbol = input("Pick an operation: ")
    num_2 = float(input("Enter the next number: "))
    answer = result(num_1, num_2)
    print(f"{num_1} {operation_symbol} {num_2} = {answer}")
    
    continue_value = input(f"Type 'yes' to continue calculating {answer}, or type 'no' to start a new calculation: ").lower()
    
    if continue_value == "no":
      continue_calculation = False
      clear()
      calculator()
    else:
      num_1 = answer

calculator()