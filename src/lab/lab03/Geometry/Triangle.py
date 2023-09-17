from Point import Point

class Triangle:
    def __init__(self,
                 point_1 = Point(0, 0),
                 point_2 = Point(1, 0),
                 point_3=Point(1, 0)
                 ) -> None:
        d1 = point_2.distance(point_3)
        d2 = point_1.distance(point_3)
        d3 = point_2.distance(point_1)
        triangle_condition = (d1 + d2 > d3) and (d1 + d3 > d2) and (d2 + d3 > d1)
        if triangle_condition:
            self.point_1 = point_1
            self.point_2 = point_2
            self.point_3 = point_3
        else:
            raise AttributeError