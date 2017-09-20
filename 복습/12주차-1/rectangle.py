class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def show_info(self):
        print("Width : ", self.width)
        print("Height : ", self.height)

    def calc_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height 
