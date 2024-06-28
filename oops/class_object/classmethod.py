class laptop():
    chargertype="ctype"

    def __init__(self):
        self.brand=""
        self.price=34

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        print(self.price)


    #by decorators
    @classmethod #another method to use class method
    def changechargertype(cls):
        cls.changechargertype="b type"
        print("charger type is changed")

    #static 
    @staticmethod
    def info():
        print("this is laptop class ")

hp=laptop()
hp.setPrice(200)
hp.getPrice()

# laptop.changechargertype(laptop)  #one method
laptop.changechargertype() 