import pandas as pd

nato_alpha = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

continue_loop = True

def generate_nato():
    user_input = input("Enter a word: ").upper()
    try:
        out_phonetic = [phonetic_dict[keys] for keys in user_input]

    except KeyError:
        print("Sorry! Only alphabets are allowed as input")
        generate_nato()

    else:
        print(out_phonetic)

generate_nato()