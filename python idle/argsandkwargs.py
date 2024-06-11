# args - no of arguments we don't know - *args - get as tuple - non keyword 

def my_function(*num):
    print(type(num))
    sum=0
    for n in num:
        sum=sum+n
    print(sum)
    
my_function(1,2,3,4)


# kwargs - keyword arguments - **kwargs - get as dictionary 

def my_function(**num):
    print(type(num))
    print(num)
    for i in num:
        print(i)
my_function(name="sangeetha",age=32,blood="o-")
