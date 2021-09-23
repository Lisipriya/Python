sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
splitted_word = sentence.split()
result = {item:len(item) for item in splitted_word}

print(result)

