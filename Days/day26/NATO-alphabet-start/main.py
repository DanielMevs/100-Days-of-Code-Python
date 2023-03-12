import pandas


with open("nato_phonetic_alphabet.csv") as f:
    nato_dict = {line.split(',')[0]: line.split(',')[1].strip() for line in f.readlines()}

print(nato_dict) 

# - Alternatively

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
