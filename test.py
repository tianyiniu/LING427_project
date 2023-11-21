# with open ("RuleBasedLearnerEnglishFiles/CELEXPrefixStrip.in", "r", encoding="cp1255") as f: 
#     text = f.read()
#     print(text[200:300])
    # line = f.readline()
    # while "Input forms:" not in line:
    #     line = f.readline()
    # line = f.readline()
    # line = line.strip("\n").split("\t")[0]

# print(line) 
# for char in line:
#     print(f"{char}: {ord(char)}")

with open ("RuleBasedLearnerEnglishFiles/CELEXPrefixStrip.fea", "r", encoding="cp1255") as f: 
    text = f.readlines()
    for line in text:
        print(line)