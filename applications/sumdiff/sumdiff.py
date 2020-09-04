# python3 applications/sumdiff/sumdiff.py

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

q = set(range(1, 10))
# q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def sumdiff(num_list):
    dict_ = {}
    for num in num_list:
      dict_[num] = f(num)

    cache_sum = {}
    dl = list(dict_.items())
    for key in dict_:
      for j in range(len(dl)):
        key1 = str(key)+','+str(dl[j][0])
        key2 = str(dl[j][0])+','+str(key)  
        if key1 or key2 not in cache_sum:
            cache_sum[key1] = dict_[key] + dl[j][1]

    cache_diff = {}
    dl = list(dict_.items())
    for key in dict_:
      for j in range(len(dl)):
        key1 = str(key)+','+str(dl[j][0])
        key2 = str(dl[j][0])+','+str(key)  
        if key1 or key2 not in cache_diff:
            cache_diff[key1] = dict_[key] - dl[j][1]

    for key1, value1 in cache_sum.items():
      for key2, value2 in cache_diff.items():
        if value1 == value2:
            for i in range(len(key1)):
                if key1[i] == ',':
                    comma = i
                    key01 = key1[:comma]
                    key11 = key1[comma+1:]

            for i in range(len(key2)):
                if key2[i] == ',':
                    comma = i
                    key02 = key2[:comma]
                    key12 = key2[comma+1:]

            print("f({key1_}) + f({_key1}) = f({key2_}) - f({_key2})    {a} + {b} = {c} - {d}".format(key1_=key01, _key1=key11, key2_=key02, _key2=key12, a=dict_[int(key01)], b=dict_[int(key11)], c=dict_[int(key02)], d=dict_[int(key12)]))


sumdiff(q)