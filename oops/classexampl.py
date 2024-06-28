#class with example
class student:
    def __init__(self):
        self.name="sangeetha"
        self.registerNO=38
    def display(self):
        print("name:",self.name)
        print("register no:" ,self.registerNO)

s1=student()
s2=student()
s1.name="karthik"
s1.registerNO=1

s2.name="vidhya"
s2.registerNO=2

print(s1.name)
print(s1.registerNO)

s1.display()
s2.display()

#passing as argument and parameter

class fruit:
    def __init__(self,colour):
        self.colour=colour


apple=fruit("red")

print(apple.colour)

#
class teacher:
    def __init__(self,name,register):
        self.name=name
        self.register=register
    def display(self):
        print("Name:",self.name)
        print("Register:",self.register)
t1=teacher("sangeetha",38)
t2=teacher("john",37)

t1.display()
t2.display()

#calculator

class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
        print("sub",self.num1-self.num2)
    def mul(self):
        print("mul",self.num1+self.num2)
    def div(self):
        print("div",self.num1+self.num2)

obj1=calculator(1,2)
obj1.add()


#another method

class calculator:
    def add(self, a,b):
        print("add",a+b)
obj1=calculator()
obj1.add(2,5)

