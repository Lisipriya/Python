import pandas as pd
# TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}

nato_alpha = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
# method 1:
# out_phonetic = [phonetic_dict[keys] for letter in user_input for keys in phonetic_dict if letter == keys]
# method 2:
out_phonetic = [phonetic_dict[keys] for keys in user_input]
print(out_phonetic)
