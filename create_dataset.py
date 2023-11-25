import sys
from clear import clear
clear() # Clear terminal output

FILEPATH = "data/deu"
WRITE_PATH = "data/deu_nouns.txt"

writes = []
lemmas = set()
word_classes = set()
cases = set()
genders = set()
numbers = set()

with open(FILEPATH, "r", encoding="utf-8") as f: 
    for line in f.readlines():
        # sichtbar	sichtbarer	ADJ;NOM;MASC;SG (ADJ;NOM;SG)
        sg, pl, features = line.split("\t")
        features_split = features.split(";")
        if len(features_split) == 4:
            word_class, case, gender, number = features_split
            number = number.strip("\n")
        elif len(features_split) == 3:
            word_class, case, number = features_split
            gender = None
            number = number.strip("\n")

        lemmas.add(sg)
        word_classes.add(word_class)
        cases.add(case)
        if gender:
            genders.add(gender)
        numbers.add(number)

        if case == "NOM" and number == "PL" and word_class == "N":
            writes.append(line)

with open(WRITE_PATH, "w", encoding="utf-8") as f:
    print(len(writes))
    f.writelines(writes)

print(len(lemmas))
print(word_classes)
print(cases)
print(genders)
print(numbers)
        