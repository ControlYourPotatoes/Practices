
class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self, width, height):
        return width * height

    def is_square(self, width, height):
        if width == height:
            return True
        else:
            return False
