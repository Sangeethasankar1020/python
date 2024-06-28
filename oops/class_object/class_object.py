

class goa: 
  name="random"
  drink= "" 
  def party(self):
    print("lets party")
  def beach(self):
    print("enjoying the beach")
    
ramesh =  goa() 
suresh = goa()

ramesh.party()
suresh.beach()

ramesh.name= "ramesh"
print(ramesh.name)
suresh.name= "suresh"
print(suresh.name)
ramesh.drink="yes"
suresh.drink="no"


#class with init

class laptop:
  def __init__(self):
    self.price=0
    self.ram=""
    self.processor=""
  def display(self):
    print("ram",self.ram)
    print("processor",self.processor)
    print("price ",self.price)
hp=laptop()
dell=laptop()

hp.price=20000
hp.ram="8gb"
hp.processor="i5"

dell.ram="6gb"
dell.price=3000
dell.processor="i4"
hp.display()
dell.display()