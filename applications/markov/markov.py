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
        punc = '.?!'

        word = random.choice(list(dict_.keys()))
        while  word[0].isupper() == False or word[0] != '"' and word[1].isupper() == False:
            if word[0].isupper() == True or word[0] == '"' and word[1].isupper() == True:
                break
            word = random.choice(list(dict_.keys()))
        k.append(word)

        word = random.choice(list(dict_[word]))

        while word[-1] not in punc or word[-1] != '"' and word[-2] not in punc:
            if word[-1] in punc or word[-1] == '"' and word[-2] in punc:
                break
            if word in dict_:
                word = random.choice(list(dict_[word]))
                k.append(word)
            else:
                word = random.choice(list(dict_.keys()))

        sentences.append(k)
    
    return sentences
        # word = random.choice(list(dict_.keys()))
        # while num_words < length:
        #     k.append(word)
        #     num_words += 1
        #     if word not in words_dict:
        #         word = random.choice(list(dict_.keys()))
        #     else:
        #         word = random.choice(list(dict_[word]))
        # sentences.append(k)
    

for i in write_sent(5, dict_):
        separator = ' '
        print((separator.join(i)).capitalize(),'\n----\n')


