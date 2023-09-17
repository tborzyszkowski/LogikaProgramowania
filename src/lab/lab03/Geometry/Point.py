import math

class Point:
    def __init__(self, x_coordinate = 0, y_coordinate = 0) -> None:
        self.x = x_coordinate
        self.y = y_coordinate

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x if x >= 0 else -x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if y >= 0 else -y

    def distance(self, point):
        dist_x = point.x - self.x
        dist_y = point.y - self.y
        dist_x_sqr = dist_x * dist_x
        dist_y_sqr = dist_y * dist_y
        return math.sqrt(dist_x_sqr + dist_y_sqr)