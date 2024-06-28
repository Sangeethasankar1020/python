#super keyword
class a():

    def __init__(self):
        print("a")
    def display(self):
        print("you are in class a ")

class b(): #inheriting class a
    def __init__(self):
        #we are using a class a constructor using super keyword.
        super().__init__()
        print("b")
    def display(self):
        print("you are in class b ")
#using multiple inheritance - use pana it take left - so we give b, a 
class c(b,a): 
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("you are in class c ")





obj1=c() #creating a obj for class c

