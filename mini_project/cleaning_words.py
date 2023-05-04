

"================================================================="
import os

"================================================================="
# Functioner

def read_from(path):
    " Funktion som läser in en angiven file och tar endast latinska bokstäver med mellan slag och apostrofer"
    
    
    char_list = []                                                           # listan där orden kommer att läggas

    with open(path,'r', encoding='utf-8') as file:                                      # öppnar filen
        for line in file:                                                                        # rad för rad
            char_str = ""                                                                       # en ny tom string
            for char in line:                                                                    # tecken för tecken
                if ord(char) in range(ord('a'),ord('z')+1) or ord(char) in range(ord('A'),ord('Z')+1) or char == "'":   # ascii table och apostrof
                    char_str += char                                                                                # addera tecknet till stingen
                else:
                    char_str += ' '                                                             # om tecknet inte uppfyller kraven lägg ett mellan slag
            char_list.extend(char_str.split())                                                  # stringen splittas och adderas till listan 

    return char_list                                                                    # retunerar en lista med ord för vidare behandling 

def apos(word):
    "Funktion som ska ta bort alla apostrofer från början eller slutet av ett ord"

    while  word.endswith("'") or word.endswith(" "):                                                     # så länge ordet slutar med apostrof
        word = word[0:len(word)-1]                                                                        # ordet blir den samma minus det sista tecknet
                                            
    while word.startswith("'") or word.startswith(" "):                         # så länge ordet börjar med apostrof
        word = word[1:]                                                             # ordet är den samma minus det första tecknet
    return word                                                                   # retunerar ordet

def same(word):     
    "Function som kollar om ordet består av samma bokstäver"

    g = False                   # bool variabel
    if len(word) <= 1: pass             # om ordet är en bokstav gör inget
    elif len(word) == 2 and word[0].lower() == word[1].lower():         # om ordet består av 2 bokstäver jämför dom ifall dom är sammma
        g = True        # samma bokstäver retunerar True
    elif len(word) == 3 and word[0].lower() == word[1].lower() == word[2].lower(): # om ordet består av 3 bokstäver jämför dom ifall dom är sammma
        g = True        # samma bokstäver retunerar True
   
    else:                           # om ordet är längre än 3 bokstäver 

        ww = len(word)                 
        ss = word[0]        
        tt = ww*ss                      # ta första bokstave gånger antalet bokstäver i ordet
        
        if word.lower() == tt.lower() :         # om det nya ordet är den samma 
            g = True                            # retunerar True
                
            

    return g                                # retunera bool

def blandat(word):
    "en Funktion för att kolla om ordet består av blandade stora och små bokstäver"


    words = ["iPhone", "iPod","MacBook","iPad","NewYork"]    # undantag
    x = word[::-1]   # ordet baklänges till vidare behandling
    if word in words:           # om ordet är en av de undantagna orden
        return False            
    elif word.startswith('Mc'):         # Om ordet börjar på Mc ( eftersom det finns många efternamn som gör )
        if len(word) == 2:              # om ordet består av 2 bokstäver som är då Mc
            return False                
        else:                           # om ordet är längre än 2 bokstäver 
            if len(word) == 3:          # om det är 3 
                return True             # finns inga ord som börjar med Mc och består av endast 3 tecken enligt min deffinition
            elif word[2] == word[2].upper() and word[3:] == word[3:].lower():           # om 3dje bokstaven är stor och resten är litet då är det ett efternamn och då är det inte blandat
                return False
    elif word.endswith("'s") and x[2:] == x[2:].upper():                # om ordet slutr med ('s) som i TV's den är inte blandad
        return False
    else:
        if len(word) >= 2:                                               # om ordet är 2 eller 1 bokstav
            if word[0] == word[0].upper() and word[1:] == word[1:].lower():         
                    
                return False

            elif word == word.upper() or word == word.lower():              # pm hela ordet är stort eller hel ordet är litet
                return False
            else:
                    
                return True
    
def spl(word):
    "function för att splita orden som sitter ihop, funktionen tar in ett ord och retunerar en lista"


    re_word = ""                                                        # ny tom string
    words = ["iPhone", "iPod","MacBook","iPad","NewYork"]               # undantag
    x = word[::-1]   # ordet baklänges till vidare behandling
    if word in words:
        return [word]                                                   # om ordet är av undantagen retunera ordet som lista
    elif word.endswith("'s") and x[2:] == x[2:].upper():                # om ordet slutar med ('s) och ordet reversad från 3de bokstaven är stora # retuneras ordet i en lista
        return [word]                                                     
    else:
        if word[0] == word[0].upper() and word[1:] == word[1:].lower():                             # om endast första bokstaven är stor 
            
            return [word]

        elif word.upper() == word or word.lower() == word:                                          # om ordet är stora eller små bokstäver
            
            return [word]
            
        else:    
            index = 0                   # en räknare
            
            for c in word:                  # itterara genom ordet
                index +=1
                
                if len(word) == index:          # när den är slut
                    re_word+= c         
                else:                           
                    if c == c.lower() and word[index] == word[index].upper():           # om bokstaven är litet och bokstaven efter är stor gör ett mellanslag i mella
                        re_word += c + " "
                        
                            
                    elif c == c.upper() and word[index] == word[index].lower():         # om bokstaven är stor och bokstaven efter är litet gör ett mellanslag innan
                                    
                        re_word +=  " " + c
                                
                                
                    else:
                        re_word+= c


            check = False                                               
            for c in re_word:               # om nya stringen innehåller mellan slag
                if c == " ":
                    check = True
                    break        
            if check == True:
                return re_word.split()       # retunera en lista av splittad nysträng
            else: 
                return [re_word]

def word_(lst):
    "Funcktion som ska ta orden från den lästa filen och rengöra allt enligt min diffenition, functionen tar in en lista som innehåler strings"

    new= []                 # vart nya orden kommer hamna

    for word in lst:        

        if len(word) == 1 and word == "a" or word == "A" or word=="I":          # ord som består av en bokstav är endast A,a oc I då ska det tas med
            new.append(word)

        else:

            if word.startswith("'") == True or word.endswith("'") == True:                  # om orden börjar eller slutar med apostrof
                word = apos(word)                                                           # ordet körs med apos funktionen och outputen av den blir ordet
                if same(word) == True: word = ""                                            # om ordet består av samma bokstäver 

            if word.startswith(" ") == True or word.endswith(" ") == True:                  # om ordet börjar eller slutar med mellan slag ska det strippas 
                word = word.strip(" ")
                if same(word)== True: word = ""                                             # check om ordet är av samma bokstäver nu

            if len(word) <= 1:                                                              # om ordet är av ett tacken
                if word == "a" or word == "A" or word =="I":                                # om bokstaven är A, a eller I den tas med
                    new.append(word)                            
                    continue

                else: word = ""                                                             # annars tas den bort    
            if word == "": continue

            else:
                if word[0] == word[0].upper() and word[1:] == word[1:].lower():             # om ordet har endast första bokstaven som stor 
                    if same(word)== True: word = ""                                         # checka om alla bokstäver är samma

                if word.upper() == word or word.lower() == word:                            # om ordet är små bokstäver     
                    if same(word)== True: word = ""                                         # checka om alla bokstäver är samma
                
                else:
                    if blandat(word) == True:                                               # om ordet innehåler små eller små bokstäver
                        cc = spl(word)                                                      # splitt ordet med den split funcktion som jag skrev
                        new.extend(word_(cc))                                               # nya orden läggs till i listan efter att varje ord har gått genom denna function (recursiv)
                        word = ""                                                           # ta bort ordet efter
                        
            if word == "" or word.isspace() or len(word) == 1 and word != "a" or len(word) == 1 and word != "A" or len(word) == 1 and word != "I":
                pass
            else:
                if same == True:
                    word=""
                else:
                    if word == "":
                        pass
                    else: new.append(word)                                                  # när alla kraven uppfyllades läggs ordet till i listan
    return new                                                                              # retunerar listan med ny renade ord

"=================================================================" 
# pathes

path_eng = os.getcwd() + r'/eng_news_100K-sentences.txt'   # läs fil
path_holy = os.getcwd() + r'/holy_grail.txt'               # läs fil
path_eng_out = os.getcwd() + r'/out_put_eng.txt'           # Output file
path_holy_out = os.getcwd() + r'/out_put_Holy.txt'         # Output file

"=================================================================" 
# programmet

lst_eng = word_(read_from(path_eng))
lst_holy = word_(read_from(path_holy))

"=================================================================" 
# Saving outputs to filse

with open(path_eng_out, 'w', encoding='utf-8') as out:
    for c in lst_eng:
        out.write(c)
        out.write("\n")


with open(path_holy_out, 'w', encoding='utf-8') as out:
    for c in lst_holy:
        out.write(c)
        out.write("\n")
