class Pizza:
    def __init__(self,toppings):
        self.toppings =toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter a password")
            if password == "puneet":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert")

pizza = Pizza(["cheese","tomato"])
print (pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print (pizza.pineapple_allowed)