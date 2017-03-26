class Pizza:
    def __init__(self,toppings):
        self.toppings=toppings

    @staticmethod
    def validate_topping(topping):
        if topping== "pineappples" :
            raise ValueError("No Pineapples plz!!")
        else:
            return True

ingredients= ["cheese","onions","babycorn"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza =Pizza(ingredients)

'''  @classmethod and @staticmethod allow the use of defined in the class methods without creating an object of that class '''
