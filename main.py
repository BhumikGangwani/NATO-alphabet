import pandas

# Reads the phonetic alphabet data
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary where key: value is letter: code
phonetic_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

while True:

    # Gets a word as input from the keyboard
    word = input("Enter your word: ").upper()

    # Exception handling to ensure the word contains letters only
    try:
        phonetic_alphabet_list = [phonetic_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
    else:
        print(phonetic_alphabet_list)
        break
