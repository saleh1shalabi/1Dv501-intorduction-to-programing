
# PART 3 (3)

"================================================================="

import table as tbl
from out_put_tabel_holy import tree_holy                        # trädet av holy texten
from out_put_table_eng import tree_eng                          # trädet av eng news texten
"================================================================="

# Eng _ 10 TOP _ Freq _words
"================================================================="

big_eng = []
al_eng = tbl.get_all_pairs(tree_eng)                             # alla värden av trädet i en tuple med ordet och antal gånger den förekommer

for c in al_eng:
    if len(c[0]) > 4:                              # orden som förekommer mer än 1000 gånger och har en längd av fyra eller längre läggs till i en lista
        big_eng.append(c[1])

big_eng = list(sorted(big_eng))                                     # sortera listan
big_eng = list(reversed(big_eng))                                    # reversa listan

count = 0
big_eng_rev=[]

for c in big_eng:                                                   # hämta dom första och då kommer vara största värden av listan 
    if count <= 10:
        big_eng_rev.append(c)
        count += 1
    else: break


for s in al_eng:
    if len(s[0]) > 4 and s[1] in big_eng_rev:
        print(s[0],s[1])

            

print("=================================================================")


"================================================================="

# Holy _ 10 TOP _ Freq _wprds
"================================================================="

big_holy = []                                       
al_holy = tbl.get_all_pairs(tree_holy)                          # alla värden av trädet i en tuple med ordet och antal gånger den förekommer

for c in al_holy:                                               # orden som förekommer mer än 1000 gånger och har en längd av fyra eller längre läggs till i en lista
    if len(c[0]) > 4:
        big_holy.append(c[1])

big_holy = list(sorted(big_holy))                                   # sortera listan
big_holy = list(reversed(big_holy))                                   # reversa listan

count_ = 1
big_holy_rev=[]

for c in big_holy:                                                      # hämta dom första och då kommer vara största värden av listan 
    if count_ <= 10:
        big_holy_rev.append(c)
        count_ += 1
    else: break

                                                 # när antalet är lika många printas ordet ut
for s in al_holy:
    if len(s[0]) > 4 and s[1] in big_holy_rev:
        print(s[0],s[1])
