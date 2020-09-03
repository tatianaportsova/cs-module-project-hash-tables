# python3 applications/no_dups/no_dups.py
# python3 applications/no_dups/test_no_dups.py

def no_dups(s):
    s = s.split(' ')
    dict_ = {}
    
    for i in range(0, len(s)):
        if s[i] in dict_:
            continue
        else:
            dict_[s[i]] = i
            
    separator = ' '
    return separator.join(list(dict_.keys()))



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))