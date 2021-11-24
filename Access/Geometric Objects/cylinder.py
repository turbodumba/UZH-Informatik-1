from geometric_object import GeometricObject


class Cylinder(GeometricObject):

    def __init__(self, radius, height, color, filled):
        super().__init__(color, filled)
        self.__PI = 3.14
        self.__radius = float(radius)
        self.__height = float(height)

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height

    def get_area(self):
        area = self.__PI * self.__radius**2 + 2*self.__PI*self.__radius*self.__height
        return round(area, 2)

    def get_volume(self):
        volume = self.__PI * self.__radius**2 * self.__height
        return round(volume, 2)
