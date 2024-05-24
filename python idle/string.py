#string

#create - single , double, triple

str='sangeetha single'
str_1="sangeetha double"
str_2='''sangeetha triple'''

print(str)
print(str_1)
print(str_2)


#data type

print( type(str))
print(type(str_1))
print( type(str_2))


#accessing strings - by index method

str="geeks for geeks"
print(str[0])

#we can also access by negative index
print(str[-4])

#slicing in string
string="greeks for greeks"
print(string[2:6])
print(string[2:-2])

#reverse

print(string[::-1])






##prime

##let j=3
##let PrimeNum=(j==1)? (j==2||j==3)?(j%2==0&&j%3==0)?`not a prime number`:`prime number`:` neither prime  nor composite number`:`not a prime number`
##console.log(j, PrimeNum, "prime or not")



##let j=3
##let PrimeNum=(j==1)? (j==2||j==3)?(j%2==0&&j%3==0)?`not a prime number`:`prime number`:` neither prime  nor composite number`:`not a prime number`
##console.log(j, PrimeNum, "prime or not")

# Define the number
j = 3

# Determine if the number is prime or not
PrimeNum = (
    "neither prime nor composite number" if j == 1 else
    ("prime number" if (j == 2 or j == 3) else
     ("not a prime number" if (j % 2 == 0 or j % 3 == 0) else "prime number"))
)

# Print the result
print(j, PrimeNum, "prime or not")
