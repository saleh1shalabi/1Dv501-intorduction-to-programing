

"================================================================="
# imports

import os

"================================================================="
# Object

g = 0 # global counter

"================================================================="
# Functions 

def count_py_lines(dir_path): # function to count the writen lines in the py file
    dir_path = os.scandir(dir_path)
    r = 0                        # counter 
    for c in dir_path:                     
        if c.name.endswith(".py"):
            with open(c,'r',encoding='utf-8') as py_file: 
                for c in py_file: 
                    if not c.isspace(): # if line is not empty
                        r += 1                  
    return r    

def itii(dir_path): 
    global g
    path = os.chdir(dir_path) # change current working directory to the given path
    path = os.scandir(dir_path) # iterriting in the giving path
    g += count_py_lines(dir_path) # the value from the line counter function at the bigginge 
    x = [] 
    
    for c in path:
        if c.is_dir(): # is it a directory we found 
            if not c.name.startswith('.'):
                x.append(c)        # add it to list
    for c in x:                           
        ny_path = dir_path + '/' + c.name # assigning new path name to the subdir
        itii(ny_path)  # recurtion 
        
    return g
"================================================================="
# Pathes

path = os.getcwd() # run in the current file for test

"================================================================="
# output
print("there is", itii(path), "lines in this directory with its subdirectorys.")
