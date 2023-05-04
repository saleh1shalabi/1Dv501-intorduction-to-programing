
# PART 3 (1)
from out_put_word_set_holy import word_set_holy   # sparad output av word_set med Holy_grail texten
from out_put_word_set_eng import word_set_eng     # sparad output av word_set med english news texten
import word_set as ws 
from os import getcwd   

"================================================================="
# English news file
"================================================================="

path = getcwd() + r'/out_put_eng.txt'


print(ws.count(word_set_eng))  # 91470 words in my set 
words_eng = []

with open(path,'r') as file:
    for word in file:
        words_eng.append(word)

print(len(words_eng))   # all words = 1963867

print(len(set(words_eng)))  # same result as mine 91470

"=================================================================="

# Holy_Grail file
"=================================================================="

path2 = getcwd() + r'/out_put_Holy.txt'


print(ws.count(word_set_holy))  # 2198 words in my set 
words_holy = []

with open(path2,'r') as file:
    for word in file:
        words_holy.append(word)

print(len(words_holy))   # all words = 11287

print(len(set(words_holy)))  # same result as mine 2198