"""
Autogrammjäger	Autogrammjäger	N;NOM;MASC;SG
Autogrammjäger	Autogrammjäger	N;NOM;MASC;PL
Rautenflagge	Rautenflagge	N;NOM;FEM;SG
Rautenflagge	Rautenflaggen	N;NOM;FEM;PL
"""
from clear import clear
clear()

FILEPATH = "data/deu_nouns.txt"

CREATE_IPA = True
IPA_WRITE_PATH = "data/deu_nouns_ipa.txt"

def find_suffix(singular, plural): 
    last_char = singular[-1]
    suffix = []
    for i in range(len(plural)-1, 0, -1):
        if plural[i] == last_char:
            break
        else:
            suffix.append(plural[i])
    return "".join(suffix[::-1])

class_en = []
class_e = []
class_null = []
class_er = []
class_s = []
class_other = []

others = []
other_lines = []
with open(FILEPATH, "r", encoding="utf-8") as f: 
    lines = f.readlines()
    total_pairs = len(lines)
    for line in lines:
        sg, pl, _ = line.split("\t")
        pair = f"{sg} {pl}\n"
        suffix = find_suffix(sg, pl)
        match suffix:
            case "en":
                class_en.append(pair)
            case "n":
                class_en.append(pair)
            case "e":
                class_e.append(pair)
            case "":
                class_null.append(pair)
            case "er":
                class_er.append(pair)
            case "s":
                class_s.append(pair)
            case _:
                other_lines.append(line)
                class_other.append(pair)

with open("others.txt", "w", encoding="utf-8") as f:
    f.writelines(other_lines)

print(f"Total pairs: {total_pairs}")
print(f"-(e)n: {len(class_en)}, percentage: {100*len(class_en)/total_pairs}")
print(f"-e: {len(class_e)}, percentage: {100*len(class_e)/total_pairs}")
print(f"-null: {len(class_null)}, percentage: {100*len(class_null)/total_pairs}")
print(f"-er: {len(class_er)}, percentage: {100*len(class_er)/total_pairs}")
print(f"-s: {len(class_s)}, percentage: {100*len(class_s)/total_pairs}")
print(f"Other: {len(class_other)}, percentage: {100*len(class_other)/total_pairs}")