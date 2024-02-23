import os
import sys

import torch
from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader

from mingpt.model import GPT
from mingpt.trainer import Trainer
from mingpt.utils import set_seed, setup_logging, CfgNode as CN
set_seed(3407)

from chargpt import get_config, CharDataset

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
model.to("cuda")

def generate(model, context):
    x = torch.tensor([train_dataset.stoi[s] for s in context], dtype=torch.long)[None,...].to("cuda")
    y = model.generate(x, 25, temperature=1.0, do_sample=True, top_k=1)[0]
    completion = ''.join([train_dataset.itos[int(i)] for i in y])
    return completion.split("\n")[0]

token = "."
while True:
    token = input("Enter a word: q to quit: ")
    print(f"Context: {token}")
    if token == "q" or token == "q\n":
        print('quit')
        break
    print(generate(model, token))