import math

class Estimation:
    def __init__(self, ppm=8, time_constant=15*3.6):
        self.ppm = ppm
        self.time_constant = time_constant

    def get_direction(self, point1, point2):
        direction_str = ""
        if point1[1] > point2[1]:
            direction_str += "Gidiyor"
        elif point1[1] < point2[1]:
            direction_str += "Geliyor"
        else:
            direction_str += ""
        return direction_str
    
    def estimate_speed(self, Location1, Location2):
        d_pixel = math.sqrt(math.pow(Location2[0] - Location1[0], 2) + math.pow(Location2[1] - Location1[1], 2))
        d_meters = d_pixel / self.ppm
        speed = d_meters * self.time_constant
        return int(speed)

   
    def ccw(self, A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

    
    def intersect(self, A, B, C, D):
        return self.ccw(A, C, D) != self.ccw(B, C, D) and self.ccw(A, B, C) != self.ccw(A, B, D)

