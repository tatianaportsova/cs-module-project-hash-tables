# python3 applications/crack_caesar/crack_caesar.py

import os
import string

letters = list(string.ascii_uppercase)
actual_frecuency = {'E':11.53,'T':9.75,'A':8.46,'O':8.08,'H':7.71,
                    'N':6.73,'R':6.29,'I':5.84,'S':5.56,'D':4.74,
                    'L':3.92,'W':3.08,'U':2.59,'G':2.48,'F':2.42,
                    'B':2.19,'M':2.18,'Y':2.02,'C':1.58,'P':1.08,
                    'K':0.84,'V':0.59,'Q':0.17,'J':0.07,'X':0.07,'Z':0.03}

with open("applications/crack_caesar/ciphertext.txt") as f:
    doc = f.read()

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
def el_count(s):
    dict_ = {}
    for element in s:
        if element in letters:
            if element in dict_:
                dict_[element] += 1
            else:
                dict_[element] = 1  
    return dict_


def decipher_txt(el_dict, document):
    elements = list(el_dict.items())
    elements.sort(key=lambda i: i[1],reverse = True)
    actual_letters = list(actual_frecuency.items())

    pairs = {}
    for i in range(0, len(elements)):
        pairs[elements[i][0]] = actual_letters[i][0]

    f = open("applications/crack_caesar/output.txt","w+")

    for i in range(0, len(document)):
          if document[i] in pairs.keys():
              f.write("%s" % (pairs[document[i]]))
          else:
              punc = '\n\t\r'
              if document[i] in punc:
                  f.write("\n")
              else:
                  f.write("%s" % ([document[i]]))
    f.close()

    f = open("applications/crack_caesar/output.txt", "rt")
    t = f.read()
    punc = "[]'"
    for i in t: 
        if i in punc:
            t = t.replace(i,"")

    foutput = open("applications/crack_caesar/de_ciphertext.txt", "wt")
    foutput.write(t)

    f.close()
    foutput.close()

    os.remove("applications/crack_caesar/output.txt")

 
    
if __name__ == "__main__":
    decipher_txt(el_count(doc), doc)
