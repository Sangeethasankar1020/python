#list task in python

#task-01 even,odd store in new array

list=[2,4,7,8,10]
evenList=[]
oddList=[]
for i in list:
    if i%2==0 :
        evenList.append(i)
    else:
        oddList.append(i)
print(evenList,"even number")
print(oddList,"odd number")

#task -02 sum of array

list=[1,2,3,0]
sum=0
for i in list:
    sum=sum+list[i]
print(sum)


#task -03 product of array

list=[1,2,2,0,3]
product=1
for i in list:
    if i!=0:
        product=product*i
print(product)

#task -04 largest number

list=[1,2,3,4,5,1,1]
largest=list[0]
for i in list:
    if i>largest:
        largest=i
print("The largest number is:", largest)

#task -05 smallest number

list=[2,8,6,1]
smallest=list[0]

for i in list:
    if i<smallest:
        smallest=i
print(smallest,"smallest number in array")

#task -06 find duplicate number in list

##list=[1,1,2,3,4,4,5,6,6]
##duplicate=[]
##for i in list:
##    if i==list[i]:
##        duplicate.append(i)
##print(duplicate)

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 6]
duplicates = []
seen = []

for number in numbers:
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.append(number)

print(duplicates)



#task -07 reverse a array

##numbers = [1, 2, 3, 4, 5]
##n = len(numbers)
##for i in range(n // 2):
##    numbers[i], numbers[n - 1 - i] = numbers[n - 1 - i], numbers[i]
##print(numbers)
