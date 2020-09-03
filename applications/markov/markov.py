# python3 applications/markov/markov.py

import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# Analyze which words can follow other words
words = words.split(' ')
dict_ = {}

for i in range(0, len(words)):
    while i < len(words)-1:
        if words[i] in dict_:
            dict_[words[i]].append(words[i+1])
            i += 1
        else:
            dict_[words[i]] = []
            dict_[words[i]].append(words[i+1])
            i += 1

# Construct 5 random sentences
def write_sent(num_of_sent, words_dict):
    sentences = []
    for i in range(1, num_of_sent+1):
        k = []
        length = random.randint(1, 10)
        num_words = 0
        word = random.choice(list(dict_.keys()))
        while num_words < length:
            k.append(word)
            num_words += 1
            if word not in words_dict:
                word = random.choice(list(dict_.keys()))
            else:
                word = random.choice(list(dict_[word]))
        sentences.append(k)
    
    return sentences

for i in write_sent(5, dict_):
        separator = ' '
        print((separator.join(i)).capitalize(),"\n")
