import random

with open("nouns.txt", "r") as f:
    tmp = f.readlines()
    nouns = [n.strip() for n in tmp]
    
with open("verbs.txt", "r") as f:
    tmp = f.readlines()
    verbs = [v.strip() for v in tmp]
    
n_nouns = len(nouns)
n_verbs = len(verbs)

noun = nouns[random.randint(0, n_nouns - 1)].lower().capitalize()
verb = verbs[random.randint(0, n_verbs - 1)].lower().capitalize()

print(f"{verb} the {noun}!")