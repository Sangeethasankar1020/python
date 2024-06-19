#collection module

import collections
#namedtuple
##student=collections.namedtuple("student",["name","age","DOB"])
##
##s=student("sangeetha",19,178681)
##
##print(s)

#counter
##print(collections.Counter(['B','B','A','B','C','A','B',
##               'B','A','C']))
  
#orderedDict
 
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od =collections. OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value) 
#delete

od.pop('a')

for key, value in od.items(): 
    print(key, value) 


od['a'] = 1

for key, value in od.items(): 
    print(key, value)
















    






    
