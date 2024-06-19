# tuple
my_tuple=(1,2,3,4,5)
my_list=[]

for i in my_tuple:
    my_list.append(i)

print(my_list)

my_list.append(6)
print(my_list)
      
      
my_tuple=tuple(my_list)
print(my_tuple)
