#abstract class - having one or more methods
#abstract methods - declared but no implements(blank)

from abc import ABC ,abstractmethod

class X(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m1(self):
        pass
class Y(X):
    def m1(self):
        print("This is m1 abstract method")

obj1=Y()
obj1.m1()
