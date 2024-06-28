class phone:

    color="black" #class variables
    def __init__(self,brand,price,chargertype):
        self.brand=brand  #instance variable
        self.price=price
        self.chargertype=chargertype
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)
        print("color:",self.color)

#sudden change
phone.color="white"
samsung=phone("samsung",10000,"b type") #object creation
samsung.display()

