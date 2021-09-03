first_item = 0
second_item = 1
num_range = int(input("Enter the range of number to print in fibonacci series: "))
print(first_item)
print(second_item)
for number in range (0,num_range-2):
  fib_ser = first_item + second_item
  first_item = second_item
  second_item = fib_ser
  print(fib_ser)
