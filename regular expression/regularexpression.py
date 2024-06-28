#regular expression
#import package - re

import re

text="Welcome to santra tech"
result=re.compile("welcome ")
ans= result.search(text)
print(ans)
