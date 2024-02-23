"""Convert data/deu_nouns.txt into a formatted .txt file for minGPT". Generate train and test splits."""

# Alpha-Version-Alpha-Versionen

from math import floor
from random import shuffle, seed
seed(4)

DATA_FILE = "data/deu_nouns.txt"
OUTPUT_TRAIN_FILE = "data/gpt_train.txt"
OUTPUT_TEST_FILE = "data/gpt_test.txt"
TRAIN_TEST_SPLIT = 0.8

def find_suffix(singular, plural): 
    last_char = singular[-1]
    suffix = []
    for i in range(len(plural)-1, -1, -1):
        if plural[i] == last_char:
            break
        else:
            suffix.append(plural[i])
    return "".join(suffix[::-1])

def calculate_stats(pairs):
    N = len(pairs)
    class_en = []
    class_e = []
    class_null = []
    class_er = []
    class_s = []
    class_other = []
    for pair in pairs:
        sg, pl = pair
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
                class_other.append(pair)
    info_dict = {
        "en": round(len(class_en)/N, 3),
        "e": round(len(class_e)/N, 3),
        "null": round(len(class_null)/N, 3),
        "er": round(len(class_er)/N, 3),
        "s": round(len(class_s)/N, 3),
        "other": round(len(class_other)/N, 3)
    }
    return info_dict

with open(DATA_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()
    pairs = []
    for line in lines:
        sg, pl, features = line.strip("\n").split("\t")
        pairs.append((sg, pl))

num_train = floor(len(pairs) * TRAIN_TEST_SPLIT)
shuffle(pairs)
train_pairs, test_pairs = pairs[:num_train], pairs[num_train:]

train_stats = calculate_stats(train_pairs)
test_stats = calculate_stats(test_pairs)

print("Train stats")
print(train_stats)
print("Test stats")
print(test_stats)

with open(OUTPUT_TRAIN_FILE, "w", encoding="utf-8") as f:
    for pair in train_pairs:
        sg, pl = pair
        line = f"{sg}:{pl}\n"
        f.write(line)

with open(OUTPUT_TEST_FILE, "w", encoding="utf-8") as f:
    for pair in test_pairs:
        sg, pl = pair
        line = f"{sg}:{pl}\n"
        f.write(line)

"""
Train stats
{'en': 0.342, 'e': 0.309, 'null': 0.247, 'er': 0.039, 's': 0.043, 'other': 0.02}
Test stats
{'en': 0.335, 'e': 0.301, 'null': 0.259, 'er': 0.037, 's': 0.048, 'other': 0.02}
"""