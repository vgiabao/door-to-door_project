#!/bin/python3

class city:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def distance(self, city):
        x_distance = abs(self.x - city.x)
        y_distance = abs(self.y - city.y)
        distance = sqrt(x_distance**2 + y_distance**2)
        return distance

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


p = city()