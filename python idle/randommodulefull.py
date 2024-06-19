#random

import random
print(dir(random))


#random - as float value 0 to 1 
print(random.random())
#unifrom
print(random.uniform(1,10))
#randint
print(random.randint(1,200))
#we can give step as
print(random.randrange(100,1000,10))
#choice - it generate a randomly in group of data
a = [1, 2, 3, 4, 5,"hi"]
print(random.choice(a))
#we can get sample data in group of stored data
#negative no, upto list len

a=[1,2,3,4,5,56,6,7,7,8,10]
print(random.sample(a,3))

a=[1,2,3,4,5,56,6,7,7,8,10]
print(random.shuffle(a))
