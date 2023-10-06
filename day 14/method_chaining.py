class Burger:
    def dough(self):
        print("dough")
        return self

    def cheese(self):
        print("cheese")
        return self

    def pepperoni(self):
        print("pepperoni")
        return self
    
burger=Burger()

burger.dough() \
.cheese()\
.pepperoni()\
.dough()