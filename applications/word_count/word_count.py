# python3 applications/word_count/word_count.py
# python3 applications/word_count/test_word_count.py

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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))