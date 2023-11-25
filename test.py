with open("RuleBasedLearnerEnglishFiles/CELEXPrefixStrip.in", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print([char for char in lines[9]])