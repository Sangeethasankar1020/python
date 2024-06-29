#regular expression
#import package - re

import re

text="Welcome to santra tech sangeetha@gmail.com"
# result=re.compile("[a-zA-Z0-9]+")
# # ans= result.search(text) #one word

# ans=result.findall(text) #to search all
# print(ans)
result=re.compile("[a-zA-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]+") #gmail 

ans=result.findall(text)
print(ans)
