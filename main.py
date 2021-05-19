import pandas

# TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in (pandas.read_csv("nato_phonetic_alphabet.csv")).iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Enter word: ").upper()
"""
list_of_the_phonetic_code = []
for letter in input_word:
    phonetic_code = letter_dict.get(letter)
    list_of_the_phonetic_code.append(phonetic_code)
"""
list_of_the_phonetic_code = [phonetic_dict.get(letter) for letter in input_word]
print(list_of_the_phonetic_code)
