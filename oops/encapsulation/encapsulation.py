#encapsulation
class company():
    def __init__(self):
        self.__companyName="Google"  #private variable

    def companyName(self):
        print(self.__companyName)  #public function

c1=company()
c1.companyName()
# print(c1.__companyName)


#access modifiers
#__ - private variable - it only access in within class
#_ - proctected variable - can access within & another class also

class company():
    def __init__(self):
        self._companyName="google"  #protected variable

class b(company):
    pass

c1=company()
print(c1._companyName)

c2=b()
print(c2._companyName)