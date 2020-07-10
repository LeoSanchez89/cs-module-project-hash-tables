# Your code here
from collections import Counter

def hash_counter():
    ignored = '":;.,-+=/\|[]{}()*^&'

    with open("./applications/histo/robin.txt") as f:
        c = Counter()
        doc = f.read()
        s = doc.lower()
        s = s.translate(str.maketrans({a:None for a in ignored}))
        c += Counter(s.split())
        new_dict = dict(c)
        for w in sorted(new_dict, key=lambda x: (-new_dict[x], x)):
            print('{:17s} {:50s}'.format(w, new_dict[w]*'#'))

print(hash_counter())