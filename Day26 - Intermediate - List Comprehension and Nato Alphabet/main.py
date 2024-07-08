import pandas

project_df = pandas.read_csv("nato_phonetic_alphabet.csv")

project_dict = {row.letter: row.code for (index, row) in project_df.iterrows()}

word = input("Enter a name or a word to get phonetic for each letters: ").upper()
output_list = [project_dict[letter] for letter in word]
print(f"The phonetic words for each letters is: {output_list}")