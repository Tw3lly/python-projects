import pandas

# Create dictionary using Pandas
# 'index_col' specifies which column is used as the label, ours is the first column.
# 'squeeze' defines if data contains only one column for values. In this case there in only one column for values.
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv", index_col=0).squeeze("columns").to_dict()

# User input, convert to all caps for consistency
word_to_translate = input("What word would you like to translate? ").upper()

# Compare input list to alphabet dictionary, if they match add the value from alphabet to new list
result = [alphabet[letters] for letters in word_to_translate if letters in alphabet.keys()]

print(f"Word = {word_to_translate}\nTranslation to NATO alphabet: {' '.join(result)}")
