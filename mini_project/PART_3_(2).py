
# PART 3  (2)

"================================================================="

from os import getcwd
import table as tb
import matplotlib.pyplot as plt
from out_put_table_eng import tree_eng          # sparad output av table med english news texten
from out_put_tabel_holy import tree_holy        # sparad output av table med Holy_grail texten

"================================================================="
# ENG_words_Freq
"================================================================="

al_eng = tb.get_all_pairs(tree_eng)             # alla värden från trädet
lst_eng= []                                     # en ny tom lista

longest_eng = 0                         

for key in al_eng:
    if len(key[0])> longest_eng:                # hitta det längsta ordet från eng news
        longest_eng = len(key[0])                

for c in range(longest_eng+1):                  # en lista med lika många listor av ord längden 
    lst_eng.append([])

for key in al_eng:  
    lst_eng[len(key[0])].append(key[0])         # alla ord av samma längd hamnar i sina platser

x_eng = list(range(len(lst_eng)))               # x-axeln med så många ord längder det finns
y_eng = []                                      # y-axeln

for ind in lst_eng:                             # addera antalet or i varje lista av samma längd
    y_eng.append(len(ind))


plt.bar(x_eng,y_eng)                            # histogram ritningen
plt.title("Histogram Of Words With X Length in ENG-File")
plt.xlabel("Words Length")
plt.ylabel("Words")
plt.show()

"================================================================="

# Holy_words_Freq'
"================================================================="

al_holy = tb.get_all_pairs(tree_holy)                    # alla värden från trädet
lst_holy= []                                     # en ny tom lista

longest_holy = 0     

for key in al_holy:                             # hitta det längsta ordet från eng news
    if len(key[0]) > longest_holy:
        longest_holy = len(key[0])

for c in range(longest_holy+1):                  # en lista med lika många listor av ord längden 
    lst_holy.append([])

for key in al_holy:                              # alla ord av samma längd hamnar i sina platser
    lst_holy[len(key[0])].append(key[0])

x_holy= list(range(len(lst_holy)))                  # x-axeln med så många ord längder det finns
y_holy = []                                         # y-axeln

for ind in lst_holy:                                # addera antalet or i varje lista av samma längd
    y_holy.append(len(ind))

plt.bar(x_holy,y_holy)                              # histogram ritningen
plt.title("Histogram Of Words With X Length in Holy-File")
plt.xlabel("Words Length")
plt.ylabel("Words")
plt.show()