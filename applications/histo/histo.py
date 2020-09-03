# python3 applications/histo/histo.py

# Open the document and read the text
with open("applications/histo/robin.txt") as f:
    words = f.read()

# Count the word in the file and store the data in a dictionary
def word_count(s):
    dict_ = {}
    punc = '":;,.-+=/\|[]{}()*^&'
    spaces = '\n\r\t'
    for element in s: 
        if element in punc:
            s = s.replace(element,"") 
        if element in spaces:
            s = s.replace(element," ") 
            
    s = s.lower().split(' ')

    for i in range(0, len(s)):
        if s[i] in dict_:
            dict_[s[i]] += 1
        else:
            dict_[s[i]] = 1
            
    if "" in dict_:
        dict_.pop("")
            
    return dict_

# Print a histogram of the words and their counts in descending order
def get_hist(word_dict):
    words = list(word_dict.items())
    words.sort(key=lambda e: e[1],reverse = True)
    
    for i in words:
        space_between = (20 - len(i[0]))
        print("{key}".format(key = i[0])," "*space_between,"#"*i[1])

get_hist(word_count(words))
