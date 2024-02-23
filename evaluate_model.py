"""Evaluate model performance and write reports"""

import os
import torch
from chargpt import get_config, CharDataset
from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader
from mingpt.model import GPT
from mingpt.trainer import Trainer
from mingpt.utils import set_seed, setup_logging, CfgNode as CN
set_seed(3407)

model_path = os.path.join('./out/chargpt', "model.pt")

config = get_config()
setup_logging(config)
set_seed(config.system.seed)

# construct the training dataset
text = open('data/gpt_train.txt', 'r').read() # don't worry we won't run out of file handles
train_dataset = CharDataset(config.data, text)

# construct the model
config.model.vocab_size = train_dataset.get_vocab_size()
config.model.block_size = train_dataset.get_block_size()
model = GPT(config.model)
model.load_state_dict(torch.load(model_path))

def generate(model, context):
    x = torch.tensor([train_dataset.stoi[s] for s in context], dtype=torch.long)[None,...].to("cpu")
    y = model.generate(x, 25, temperature=1.0, do_sample=True, top_k=1)[0]
    completion = ''.join([train_dataset.itos[int(i)] for i in y])
    return completion.split("\n")[0]


def find_suffix(singular, plural): 
    last_char = singular[-1]
    suffix = []
    for i in range(len(plural)-1, -1, -1):
        if plural[i] == last_char:
            break
        else:
            suffix.append(plural[i])
    return "".join(suffix[::-1])

def get_class(suffix):
    if suffix == "en" or suffix == "n":
        return "en"
    elif suffix == "e":
        return "e"
    elif suffix == "":
        return "null"
    elif suffix == "er":
        return "er"
    elif suffix == "s":
        return "s"
    else:
        return "other"

def generate_eval(model, gold_pairs):
    N = len(gold_pairs)
    correct = 0

    class_en = {"en": [], "e": [], "null": [], "er": [], "s":[], "other": []}
    class_e = {"en": [], "e": [], "null": [], "er": [], "s":[], "other": []}
    class_null = {"en": [], "e": [], "null": [], "er": [], "s":[], "other": []}
    class_er = {"en": [], "e": [], "null": [], "er": [], "s":[], "other": []}
    class_s = {"en": [], "e": [], "null": [], "er": [], "s":[], "other": []}
    class_other = {"en": [], "e": [], "null": [], "er": [], "s":[], "other": []}

    class_name_to_dict = {"en": class_en, "e": class_e, "null": class_null, "er": class_er, "s": class_s, "other": class_other}

    class_correct = {"en": 0, "e": 0, "null": 0, "er": 0, "s": 0, "other": 0}
    class_total = {"en": 0, "e": 0, "null": 0, "er": 0, "s": 0, "other": 0}

    predictions = {}
    correct = 0
    pairs_with_novel_characters = []
    for pair in gold_pairs:
        sg, pl = pair
        context = sg+":"
        try:
            completion = generate(model, context)
        except KeyError:
            pairs_with_novel_characters.append(pair)
            continue

        prediction = find_suffix(context, completion) # Each p
        predictions[sg] = prediction

        prediction_class = get_class(find_suffix(sg, prediction))
        gold_class = get_class(find_suffix(sg, pl))

        class_total[gold_class] += 1
        if pl == prediction:
            correct += 1
            class_correct[gold_class] += 1
            continue # Skip correct predictions
        class_dict = class_name_to_dict[gold_class]
        class_dict[prediction_class].append(pair)
        
    # Write reports
    for class_name, class_dict in class_name_to_dict.items():
        report_path = f"prediction_reports/{class_name}"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"Class {class_name} has {class_total[class_name]} instances. Which is {round(class_total[class_name]/N, 3)} of the test data.\n")
            f.write(f"The model correctly predicted: {class_correct[class_name]} instances. The class accuracy is: {round(class_correct[class_name]/class_total[class_name], 3)}\n")
            f.write(f"Breakdown of all predictions:\n\n")
            for prediction_class_name, pairs in class_dict.items():
                f.write(f"Class {prediction_class_name}:\n")
                for sg, pl in pairs: 
                    f.write(f"\tSG: {sg}; PL: {pl}; PRED: {predictions[sg]}\n")

    acc = round(correct/N, 3)
    return acc, pairs_with_novel_characters



# Evaluate model performance on test set
pairs = []
with open("data/gpt_test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines: 
        sg, pl = line.strip("\n").split(":")
        pairs.append((sg, pl))

# pairs = pairs[:100] # TODO remove
acc, novel_pairs = generate_eval(model, pairs)
print(f"Accuracy: {acc}")
print(f"Novel characters")
for pair in novel_pairs:
    print(pair)
