
# Part 4 (2)

"================================================================="
# Imports

from os import getcwd
import random
import word_set as ws
from time import time
import matplotlib.pyplot as plt
from out_put_word_set_eng import word_set_eng

"================================================================="
# Functions

def adding_words_time(x):
    "Funktion som mäter tiden av att hasha och rehasha så många ord som det anges"

    global word_lst_eng                 # listan med ord
    tot = 0
    count = 0                            
    word_set = ws.new_empty_set()
    r = 0                               
    t0 = time() 
    while r != 10:
        for c in word_lst_eng:
            if count != x:
                ws.add(word_set,c)
                count += 1
            else: break
        r+=1
    t1 = time()
    tot += (t1-t0)
    return tot/10                                                      # retunerar tiden den tog

def bucket_size(x):
    "en funktion som retunerar antalet element i en hash set av angiven ord mängd"

    global word_lst_eng
    count = 0
    word_set = ws.new_empty_set()
    for c in word_lst_eng:
        if count != x:
            ws.add(word_set,c)
            count += 1
        else: break
    return ws.max_bucket_size(word_set)

"================================================================="
# List containing all unique words from english file    # 91474 Words

word_lst_eng = ws.to_string(word_set_eng).split()                   # listan med alla unika ord från eng news

"================================================================="
# Axsels
    
x = [10, 20, 40, 80, 100, 200, 300, 400]
max_bucket = []
y = []

"================================================================="
# Getting Time Of Adding Deffirent Number Of Words And Adding It To List To Be Axel When Ploting

y.append(adding_words_time(10))
y.append(adding_words_time(20))
y.append(adding_words_time(40))
y.append(adding_words_time(80))
y.append(adding_words_time(100))
y.append(adding_words_time(200))
y.append(adding_words_time(300))
y.append(adding_words_time(400))

"================================================================="
# Time To Re-hash Plot

plt.scatter(x,y, marker="o")
plt.title("Time To Re-hash")
plt.xlabel("Words")
plt.ylabel("Time")
plt.show()

"================================================================="
# Getting Max Buckets Value Of Word_sets With Deffirent Number Of Words And Adding It To List To Be Axel When Ploting

max_bucket.append(bucket_size(10))
max_bucket.append(bucket_size(20))
max_bucket.append(bucket_size(40))
max_bucket.append(bucket_size(80))
max_bucket.append(bucket_size(100))
max_bucket.append(bucket_size(200))
max_bucket.append(bucket_size(300))
max_bucket.append(bucket_size(400))

"================================================================="
# Max Bucket To Words Plot

plt.scatter(x,max_bucket)
plt.title("Max Bucket To Words")
plt.xlabel("Words")
plt.ylabel("Max Bucket")
plt.show()




