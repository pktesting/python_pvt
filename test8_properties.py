class Pizza:
    def __init__(self,toppings):
       self.toppings= toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese","tomato"])
print (pizza.pineapple_allowed)
pizza.pineapple_allowed = True

# common use of a property is to make an attribute read-only