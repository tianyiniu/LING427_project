import sys

def get_size_mb(some_obj):
    return sys.getsizeof(some_obj) / 1024**2


FILEPATH = "deu/deu_nouns"
WRITE_PATH = "deu/deu_nouns_nom"
writes = []

lemmas = set()
cases = set()
exceptions = []
with open(FILEPATH, "r", encoding="utf-8") as f: 
    for line in f.readlines():
        # sichtbar	sichtbarer	ADJ;NOM;MASC;SG
        sg, pl, features = line.split("\t")
        features_split = features.split(";")
        lemmas.add(sg)
        if len(features_split) == 4:
            word_class, case, gender, number = features_split
        elif len(features_split) == 3:
            word_class, case, number = features_split
        else:
            exceptions.append(line)
        cases.add(case)



print(len(lemmas))
print(cases)
print(exceptions)
        