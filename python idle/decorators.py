#decorators
def this_my_dec(func):
    def message():
        print("thanks for entering")
        func()
        print("byee")
    return message


@this_my_dec #we can call the decorator by two methods
def techspot():
    print("welcome to ocean academy")
#techspot=this_my_dec(techspot) #also by this methods
techspot()
