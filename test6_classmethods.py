class Rectange:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def calculate_area(self):
         return self.width * self.height

    @classmethod     # creating a class_method
    def new_square(cls,side_length):
         return cls(side_length,side_length)

square =Rectange.new_square(5)
print(square.calculate_area())   # acquiring behaviour of the class Rectangle which returns multiple of width & height

rect=Rectange(5,7)
print(rect)       # need to fix this



