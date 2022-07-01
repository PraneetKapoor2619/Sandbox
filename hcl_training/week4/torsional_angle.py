import math

class Points(object):
        def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

        def __sub__(self, no):
                obj = Points(self.getx() - no.getx(), self.gety() - no.gety(), self.getz() - no.getz())
                return obj
        
        def getx(self):
                return self.x
        
        def gety(self):
                return self.y
        
        def getz(self):
                return self.z
        
        def dot(self, no):
                return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

        def cross(self, no):
                x1, x2 = self.getx(), no.getx()
                y1, y2 = self.gety(), no.gety()
                z1, z2 = self.getz(), no.getz()
                x_component = (y1 * z2) - (y2 * z1)
                y_component = -1 * ((x1 * z2) - (x2 * z1))
                z_component = (x1 * y2) - (x2 * y1)
                return Points(x_component, y_component, z_component)

        def absolute(self):
                return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
        points = list()
        for i in range(4):
                a = list(map(float, input().split()))
                points.append(a)

        a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
        x = (b - a).cross(c - b)
        y = (c - b).cross(d - c)
        angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

        print("%.2f" % math.degrees(angle))