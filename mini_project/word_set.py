

# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements

# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets

# Adds word to word set if not already added
def add(word_set, word):
    z = bucket_list_size(word_set)                      #kolla antalet bucket
    b = contains(word_set, word)                            # kolla om ordet redab finns i word_set
    if b == True:                                           # pass om den finns 
        pass
        
    else:                           
        if count(word_set) >= z:                            # om antalet bucket inte räcker Rehasha allt och sen lägg till ordet i sin hashing värde plats
            word_set = dbl_rehash(word_set)
            index = hashing(word) % z
            word_set[index].append(word)
        else:                                                   # om det räcker med buckets hasha ordet och lägg ordet i sin hashing plats modulus antalet buckets 
            index = hashing(word) % z
            word_set[index].append(word)
 
    return word_set    # reunera hashade listan
         
# The Re-hashing Function
def dbl_rehash(word_set):    
    " re-hashing funktionen"
    lst = []                            # en ny lista
    
    for c in word_set:                          # läagg alla element i hashade listan i den nya listan
        lst.extend(c)
    b = bucket_list_size(lst) * 2                                       # fördubbla antalet bucket
    b = int(b/10)                                                   # dela med 10 säg vi hade 1280 då blir det 128

    word_set.clear()                                            # tomma vår hashade lista

    for c in range(b):                                         # addera 10 bucketes varje gång i range antal fördubblade listan delat med 10
        word_set.extend(new_empty_set())
    
    for c in lst:                                           # hasha om alla ord igen som vi tagit tidigare från hashade listan
        add(word_set,c)
            
    
    
    return word_set                                                # retunera den ny rehashade listan

# Hashing function
def hashing(word):
    "Hashing funktionen"

    word = word.lower()                                             # gör ordet till lower case detta gör att ord som Word och WORD och word får samma bucket
    x = ""                                                             
    y = 0
    for c in word:                                                          # addera ascii värdet som str säg vi har AB som ord dett får värdet 9293 alltså de adderas inte
        x += str(ord(c))
    for c in word:                                                                  # addera ascci värden till varandra som AB får värdet 93 + 92 = 185 sedan dela värdet med två
        y += (ord(c)) 
    y = round(y/2)
    
    return int(x) % (y)                                 # retunera modulus integer den stora talet med y


# Returns current number of elements in set
def count(word_set):
    x = 0
    for c in word_set:  # gå in i varje bucket i Hahade listan och addera antalet element i varje bucket
        x+= len(c)
    return x                            # retunera antalet

# Returns current size of bucket list
def bucket_list_size(word_set):
                                                # räkna antalet buckets i listan
    return len(word_set)
   

# Returns a string representation of the set content
def to_string(word_set):
    result = ""
    for c in word_set:                      # i varje bucket addera alla värden till stringen
        for s in c:
            result += str(s) + ' '
        
    return result                           # retunera stringen
    


# Returns True if word in set, otherwise False    
def contains(word_set, word):

    index = hashing(word) % bucket_list_size(word_set)                                  # få ut hashing värdet och modulus antal buckets får vi veta vart ordet skulle vara 

    b = False
    if word in word_set[index]:                                             # checka om ordet är där och retunera true eller false
        b =  True
    return b


# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word):
    x = hashing(word)                                               # få hashing värdet av ordet och modulus antal bucket ska ordet vara där
    b = bucket_list_size(word_set)
    index = x % b

    if word in word_set[index]:                                         # om ordet finns radera den
        word_set[index].remove(word)

    return word_set
    

# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    x = 0                                       # räkna antalet element i varje bucket och retunera den största 
    for c in word_set:
        t = len(c)
        if t > x:
            x = t
    
    
    return x




