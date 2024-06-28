#inheritance
#parent - child like that 
#using another class 
# class dad():
#     def phone(self):
#         print("dads phone")
# class mom():
#     def sweet(self):
#         print("mom having sweet")     

# class son(dad,mom): #passing dad class as parameter  - single inheritance 
#     def laptop(self):
#         print("sons laptop")



# #creating object for son
# ram=son()
# ram.laptop()

# ram.phone()
# ram.sweet()


# class grandpa():
#     def phone(self):
#         print("grandpa phone")

# class dad(grandpa):
#     def money(self):
#         print("dad money")

# class son(dad):
#     def laptop(self):
#         print("son laptop")

# ram=son()

# ram.laptop()
# ram.money()

# #creating object for dad to use grandpa phone
# d1=dad()
# d1.phone()
# ram.phone()


#heirachy inheritance
class dad():
    def money(self):
        print("money")

class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

s2=son2()
s2.money()

