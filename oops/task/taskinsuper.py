# class shape():
#     def area(self):
#         return 0

# class rectangle(shape): #inheritance
#     #overriding
#     def area(self):
#         l=10
#         b=20
#         print(l*b,"area of rectangle")


# s1=shape()
# print(s1.area())

# r1=rectangle()
# r1.area()


#task 2

class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)         #getting name from class person using super keyword
        self.grade=grade
        print(grade)

    def display(self):
        print("name:",self.name)
        print("grade:",self.grade)

s1=student("john","A")
s1.display()


#task 3

class employe():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employe):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def manager(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("department:",self.department)

p1=manager("Sangeetha",200000,"Data science")
p1.manager()