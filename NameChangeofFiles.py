# -*- coding: utf-8 -*-
"""
Below python script will read each files from specific folder and  modifies the naming convention of 
each files(format : filename with date modified time)

script will get stuck if there is any duplicate filename
"""
# C:\Users\XXXXXX\Documents\1\11

import os
import datetime
target ="C:/Users/XXXXXX/Documents/1/11/"

os.chdir(target)
allfiles = os.listdir(target)
count = 0

for filename in allfiles:
    count = count + 1
    fcount=len(allfiles)
    
    if not os.path.isfile(filename):
        continue
    t = os.path.getmtime(filename)
    v= datetime.datetime.fromtimestamp(t)
    x = v.strftime('%Y%m%d%H%M')
    
    bb =filename.split("_")
    string = '_'.join(str(x) for x in bb[0:6]) 

    temp_name = str(string) + ".csv" + "_" + x
    #print(temp_name)
    print("count:",count,"_",fcount,temp_name,"completed") 

    while filename != temp_name:
        if not os.path.exists(temp_name):
            os.rename(filename, temp_name)
            filename = temp_name
        else:
            temp_name = str(string) + ".csv" + "_" + x
