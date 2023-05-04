# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child


# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]

# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root,key,value):
    node = root 
    if node[0] == None:                             # om första platsen i noden är none adderas key till den och value till andra platsen
        node[0] = key               
        node[1] = value
    elif  node[0] == key:                               # om ordet finns redan uppdateras value endast
        node[1] = value
    else:
        if node[0] > key:                               # om nya ordet är mindre kollas 3de platsen 
            if node[2] == None:                         # om den är none adderas en ny root där och key och value läggs i första och andra platsen
                node[2] = new_empty_root()
                add(node[2],key,value)
            else: add(node[2],key,value)                  # om det inte är none körs det recursivt som denna platsen som root
        elif node[0] < key:                                 # om key är större checkas 4de platsen
            if node[3] == None:                             # om den är none adderas en ny root. key och value får ha första och andra platsen i den
                node[3] = new_empty_root()
                add(node[3],key,value)
            else: add(node[3],key,value)                    # om den inte är none körs det rucursivt med 4de platsen som root
    
    return root                                                 # retunerar trädet

# Returns a string representation of the table content.
# That is, all key-value pairs

def to_string(root):
    lst = []                        
    g = None
    if root[2] != None:
        g = (get_all_pairs(root[2]))        # ta alla värden från vänster och addera dem till en tuple 
        for c in g:                             # addera varje värde i tuplen till listan
            lst.append(c)
        g = None    

    if root != None:                            # ta första och andra värden och addera dem till listan
        g = (root[0], root[1])
        lst.append(g)
        g = None
        
    if root[3] != None:                                 #alla värden från höger i en tuple som sedan läggs till i listan
        g = (get_all_pairs(root[3]))
        for c in g:
            lst.append(c)
        g = None

    string = ""
    for c in lst:                           # alla elements från listan görs till string
        string += str(c) + " "
           
    return string                                       # retunera stringen

# Returns the value for the given key. Returns None if key doesn't exists.

def get(node,key):
    g = None                        
    if node != None:                    # kollar om trädet inte är tom
        if node[0] != None:                 

            if key == node[0]:                          # om värdet där är ordet som söks tar vi value
                g = node[1]
                
            elif key < node[0]:                                 # annars kollar vi om det är mindre än värdet och kör recursivt på tredje platsen som node
                g = get(node[2],key)

            elif key > node[0]:                                     # annars kollar vi om det är större än värdet och kör recursivt på 4de platsen som node
                g = get(node[3],key)       
    
    return g                                            # retunerar value om den hittades ammars förblir det none

# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.

def max_depth(node):
    left, right = 1, 1                              # variabler till höger och vänster längdet
    if node != None:                                    # om node inte är 0 då är vi inte på slutet
        if node[2] != None:                                     # om 3de platsen inte är none då går den in recursivt där och adderar en varje gång
            left += max_depth(node[2])
        if node[3] != None:                                         # om 4de platsen inte är none då går den in recursivt och adderar till höger värdet
            right += max_depth(node[3])    
                                        # jämförelse mellan höger och vänster längder för att retunera det större
    if left > right:
        return left
    elif right > left:
        return right
    else:                                   # om dem är samma retuneras en av dom  
        return left

# Returns the number of key-value pairs currently stored in the table

def count(node):
    tot = 0             # räkne variabel
    if node != None:                        # så länge node inte är none då är trädet inte slut
        tot +=1                                 # addera en som är då första värdet
        if node[2] != None:                                     # kolla vänster och addera recursivt alla värden
            tot += count(node[2])
        if node[3] != None:                                 # kolla höger och addera recursivt alla värden
            
            tot += count(node[3])
    return tot                          # retunera antalet

# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order

def get_all_pairs(root):
    lst = []
    g = None
    
    if root[2] != None:                                                 # ta alla värden från vänster och addera dem till en tuple 
        g = (get_all_pairs(root[2]))
        for c in g:
            lst.append(c)                                   # addera varje värde i tuplen till listan
        g = None

    if root != None:                                        # ta första och andra värden och addera dem till listan
        g = (root[0], root[1])
        lst.append(g)
        g = None
                                                                                #alla värden från höger i en tuple som sedan läggs till i listan
    if root[3] != None:
        g = (get_all_pairs(root[3]))
        for c in g:
            lst.append(c)
        g = None
    

    return lst   # Retunerar listan med tuplar i 
    
 

