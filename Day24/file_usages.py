# For reading the file
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

# For writing the text in the file
with open("my_file.txt", "a") as file:
    file.write("\nLives in Chennai")

# For creating the new file
with open("my_new_file.txt", "w") as file:
    file.write("Hello World")

# Use of absolute path
with open("/Users/lisipriya/Desktop/my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

# Use of relative path
with open("../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
