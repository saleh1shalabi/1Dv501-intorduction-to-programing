

"================================================================="
# Imports

import os
import table as tbl

"================================================================="
# root för träden som kommer byggas

root_Holy = tbl.new_empty_root() 
root_eng = tbl.new_empty_root()

"================================================================="
# pathes till filerna som jag läser ifrån

path_eng = os.getcwd() + r'/out_put_eng.txt'
path_holy = os.getcwd() + r'/out_put_Holy.txt'

"================================================================="
# pathes till nya filer som jag ska skriva till

path_output_holy = os.getcwd() + r'/out_put_tabel_holy.py'
path_output_eng = os.getcwd() + r'/out_put_tabel_eng.py'

"================================================================="
# tomma strängar

holy = ""
eng = ""

"================================================================="
# inläsning från filerna// alla ord läggs till i stringarna

with open(path_holy,'r',encoding='utf-8') as file:
    for c in file:
        holy += c

with open(path_eng,'r',encoding='utf-8') as file:
    for c in file:
        eng += c

"================================================================="
# splita stringarna och göra till listor

eng = eng.split()
holy = holy.split()

"================================================================="
# bygga träden av alla orden i listorna

for c in holy:
    tm = tbl.get(root_Holy,c)           # hämta value av ordet
    value = 1                               
    if tm != None:                      # om value är inte none
        new = value+tm                      # aderas det befintliga value med 1 och läggs till igen
        tbl.add(root_Holy,c,new)             
    else:                                       # annars är value bara 1
        tbl.add(root_Holy,c,1)


for c in eng:                           
    tm = tbl.get(root_eng,c)                # hämta value av ordet
    value = 1
    if tm != None:                           # om value är inte none
        new = value+tm                              # aderas det befintliga value med 1 och läggs till igen
        tbl.add(root_eng,c,new)
    else:
        tbl.add(root_eng,c,1)                               # annars är value bara 1

"================================================================="
# utskrivning av träden till nya filerna 
# senare för man gå in och konventera träden till listor # alltså att ange dom som variabler


with open(path_output_holy,'w', encoding='utf-8') as c:
    c.write(str(root_Holy))


with open(path_output_eng,'w', encoding='utf-8') as c:
    c.write(str(root_eng))


