
#return - function call values return , code execusion stop
#return in args
def my_function(*num):
    print(type(num))
    sum=0
    for n in num:
        sum=sum+n
    return sum
    # print(sum)
    
print(my_function(1,2,3,4))

# return in kwargs 

def my_function(**num):
    print(type(num))
    print(num)
    for i in num:
      print(i) 
print(my_function(name="sangeetha",age=32,blood="o-"))

#return 

def my_function(**num):
    print(type(num))
    print(num)
    key = []
    for i in num:
        key.append(i)
    return key

print(my_function(name="sangeetha", age=32))






