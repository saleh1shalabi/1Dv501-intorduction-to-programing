import word_set as ws
from time import time
import os
t0 = time()

# path_holy = os.getcwd() + r'/out_put_Holy.txt'
# path_holy_out = os.getcwd() + r'/out_put_word_set_holy.txt'

path = os.getcwd() + r'/out_put_eng.txt'
path2 = os.getcwd() + r'/out_put_word_set_eng.py'

words = ws.new_empty_set()

e = ""

with open(path,'r', encoding='utf-8') as c:
    for s in c:
        e += s

x = e.split()


for c in (x):
    ws.add(words,c)

t1 = time()
with open(path2,'w', encoding='utf-8') as c:
    c.write(str(words))

tot = t1-t0
print(tot)

print(ws.count(words))
print(len(set(x)))
