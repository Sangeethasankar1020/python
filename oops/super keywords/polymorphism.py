#polymorphism
# def add(a,b,c=0):
#     print("add",a+b+c)
# add(2,4,5)
# #we can reassign that value
# def add(a=10):
#     print(a)
# add(30)


#animal task

class animal():
    def sound(self):
        print("animal makes sound")
class dog(animal):
    #method overriding previous method 
    def sound(self):
        print("dog barks")

class bird(animal):
    def sound(self):
        print("birds ")

# a1=animal()
# a1.sound()

#dog obj
# d1=dog()
# d1.sound()

#birds obj

b1=bird()
b1.sound()