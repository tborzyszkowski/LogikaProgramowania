from Point import Point

class Segment:
    def __init__(self, point_1 = Point(0, 0), point_2 = Point(1,1)) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def lenght(self):
        #return 0
        return self.point_1.distance(self.point_2)