class Rectangle():
    def __init__(self, width, height):
        self.side = None
        self.width = width
        self.height = height
    def __repr__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
    def set_width(self, width):
        self.width = width
        if self.__class__ == Square:
            self.height = width
            self.side = width

    def set_height(self, height):
        self.height = height
        if self.__class__ == Square:
            self.width = height
            self.side = height
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self. perimeter
    def get_diagonal(self):
        self.diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return self.diagonal
    def get_picture(self):
        if (self.width or self.height) > 50:
            return "Too big for picture."
        picture = ''
        for lines in range(self.height):
            picture += "*" * self.width
            if lines < self.height:
                picture += "\n"
        return picture
    def get_amount_inside(self, new_shape):
        total_capacity = 0
        if self.width > new_shape.width:
            width_capacity = self.width // new_shape.width
            if self.height > new_shape.height:
                height_capacity = self.height // new_shape.height
                total_capacity = width_capacity * height_capacity
        return total_capacity

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    def __repr__(self):
        return f'{self.__class__.__name__}(side={self.side})'
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
