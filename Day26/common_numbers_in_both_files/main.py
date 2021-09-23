f1 = open("file1.txt")
file1 = f1.readlines()
f2 = open("file2.txt")
file2 = f2.readlines()
# Write your code above 👆
result = [int(number) for number in file1 if number in file2]
print(result)


