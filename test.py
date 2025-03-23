def syllable_count(word):
    count = 0
    count2 = 0
    vowels = "aeiouy"
    vowels2 = "aeiou"
    
    if word[0] in vowels:
        count += 1
    
    if word[0] in vowels2:
        count2 += 1
    
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
        
        if word[index] in vowels2 and word[index - 1] not in vowels2:
            count2 += 1
    
    if word.endswith("e"):
        count -= 1
        count2 -= 1
    
    if count == 0:
        count += 1
    
    if count2 == 0:
        count2 += 1
    
    if count < count2:
        return count
    
    return count2

import bisect
from nltk.corpus import wordnet as wn

nouns = []
for synset in list(wn.all_synsets('n')):
    for lemma in synset.lemmas():      
        noun = lemma.name().lower()
        if noun.isalpha() and syllable_count(noun) == 1 and noun not in nouns:
            bisect.insort(nouns, noun)
            
with open('nouns.txt', 'w') as f:
    for noun in nouns:
        f.write(f"{noun}\n")

verbs = []
for synset in list(wn.all_synsets('v')):
    for lemma in synset.lemmas():      
        verb = lemma.name().lower()
        if verb.isalpha() and len(verb) < 10 and verb not in verbs:
            bisect.insort(verbs, verb)
            
with open('verbs.txt', 'w') as f:
    for verb in verbs:
        f.write(f"{verb}\n")
