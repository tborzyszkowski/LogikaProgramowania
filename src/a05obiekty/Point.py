from math import sqrt

class Point:
    def __init__(self, x_coordinate = 0, y_coordinate = 0, z_coordinate = 0) -> None:
        self.x = x_coordinate
        self.y = y_coordinate
        self.z = z_coordinate

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x if x>=0 else -x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if y >= 0 else -y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z if z >= 0 else -z

    def distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        dz = self.z - point.z
        return sqrt(dx*dx + dy*dy + dz*dz)