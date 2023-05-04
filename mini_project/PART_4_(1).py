
# Part 4 (1)

"================================================================="
# Imports

from os import getcwd
from random import randint
import table as tbl
from time import time
from out_put_table_eng import tree_eng
import word_set as ws
from out_put_word_set_eng import word_set_eng
import matplotlib.pyplot as plt

"================================================================="
# List containing all unique words from english file    # 91470 Words

word_lst_eng = ws.to_string(word_set_eng).split()                           # en lista med alla unika ord från eng news
"================================================================="
#Functions

def tree_making(lst,b):
    "function som bygger upp träd av en lista med ord och hur stort trädet ska bli"

    x = 0
    tree = tbl.new_empty_root()
    for c in lst:
        if x != b:
            tbl.add(tree,c,1)
            x+=1
        else: break
    return tree                                             # retunerar en BST

def time_cou(lst):
    "funktion som räknar tiden det tar att hitta 20000 random ord av en lista i teädet den matas med"
    tot = 0
    global word_lst_eng
    t0 = time()
    repet = 0                                       # reptera 10 gånger för att få så nära sanningen som möjligt
    while repet != 10:
        for c in range(20000):
            x = randint(0,91469)
            tbl.get(lst,word_lst_eng[x])
        repet += 1
    t1 = time()
    tot += (t1-t0)   
    return tot/10                                      # retunerar tiden den tog
"================================================================="
# The Axsels To Plot

x = []
y = []
depth = []

"================================================================="
# Tree Making of deffirent sizes

tree_100 = tree_making(word_lst_eng,100)
tree_200 = tree_making(word_lst_eng,200)
tree_300 = tree_making(word_lst_eng,300)
tree_400 = tree_making(word_lst_eng,400)
tree_500 = tree_making(word_lst_eng,500)
tree_600 = tree_making(word_lst_eng,600)
tree_700 = tree_making(word_lst_eng,700)
tree_1000 = tree_making(word_lst_eng,1000)
tree_3000 = tree_making(word_lst_eng,3000)
tree_4000 = tree_making(word_lst_eng,4000)
tree_5000 = tree_making(word_lst_eng,5000)
tree_10000 = tree_making(word_lst_eng,10000)
tree_15000 = tree_making(word_lst_eng,15000)
tree_25000 = tree_making(word_lst_eng,25000)
"================================================================="
# Getting The Size From The Trees And Appending It To The X-Axel

size_100 = tbl.count(tree_100)
size_200 = tbl.count(tree_200)
size_300 = tbl.count(tree_300)
size_400 = tbl.count(tree_400)
size_500 = tbl.count(tree_500)
size_600 = tbl.count(tree_600)
size_700 = tbl.count(tree_700)
size_1000 = tbl.count(tree_1000)
size_3000 = tbl.count(tree_3000)
size_4000 = tbl.count(tree_4000)
size_5000 = tbl.count(tree_5000)
size_10000 = tbl.count(tree_10000)
size_15000 = tbl.count(tree_15000)
size_25000 = tbl.count(tree_25000)

x.append(int(size_100))
x.append(int(size_200))
x.append(int(size_300))
x.append(int(size_400))
x.append(int(size_500))
x.append(int(size_600))
x.append(int(size_700))
x.append(int(size_1000))
x.append(int(size_3000))
x.append(int(size_4000))
x.append(int(size_5000))
x.append(int(size_10000))
x.append(int(size_15000))
x.append(int(size_25000))

"================================================================="
# The Time It Takes To Get A 20000 Random Different Words Words Deppnding On Tree Size


y.append(time_cou(tree_100))
y.append(time_cou(tree_200))
y.append(time_cou(tree_300))
y.append(time_cou(tree_400))
y.append(time_cou(tree_500))
y.append(time_cou(tree_600))
y.append(time_cou(tree_700))
y.append(time_cou(tree_1000))
y.append(time_cou(tree_3000))
y.append(time_cou(tree_4000))
y.append(time_cou(tree_5000))
y.append(time_cou(tree_10000))
y.append(time_cou(tree_15000))
y.append(time_cou(tree_25000))

"================================================================="
# Plot Showing Of Time To Get

plt.plot(x,y, marker="o")
plt.title("Time To Get Random Deffirent Words To Tree Size")
plt.xlabel("Tree Size")
plt.ylabel("Time")
plt.show()

"================================================================="
# Getting The Max Depth of Deffirent Sized Trees And Adding It To A List

depth.append(tbl.max_depth(tree_100))
depth.append(tbl.max_depth(tree_200))
depth.append(tbl.max_depth(tree_300))
depth.append(tbl.max_depth(tree_400))
depth.append(tbl.max_depth(tree_500))
depth.append(tbl.max_depth(tree_600))
depth.append(tbl.max_depth(tree_700))
depth.append(tbl.max_depth(tree_1000))
depth.append(tbl.max_depth(tree_3000))
depth.append(tbl.max_depth(tree_4000))
depth.append(tbl.max_depth(tree_5000))
depth.append(tbl.max_depth(tree_10000))
depth.append(tbl.max_depth(tree_15000))
depth.append(tbl.max_depth(tree_25000))


"================================================================="
# Plot Showing Of Tree size To Max Depth

plt.plot(x,depth,marker="o")
plt.title("Tree Size To Max Depth")
plt.xlabel("Tree Size")
plt.ylabel("Max Depth")
plt.show()


