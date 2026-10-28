# # Write OOP Classes to handle the following scenarios: 
# A user can create and view 2D co ordinated.
# A user can find out the distance between 2 co ordinates
# A User can find the distance of a co ordinated from origin
# A user can check if a point lies on a given line
# A user can find the distance between a 2D point and a given line

class Point():

    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 +(self.y_cod-other.y_cod)**2)**0.5

    def distance_origin(self):
        return self.euclidean_distance(Point(0,0))
class Line():

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return '{}x+{}y+{}=0'.format(self.a,self.b,self.c)

    def point_on_line_check(line,point):
        if line.a*point.x_cod +line.b*point.y_cod+line.c==0:
            return "point lies on the line"
        else:
            return "Point doesnot lies on the line"

    def dist_point_line(line,point):
        return (abs(line.a*point.x_cod+line.b*point.y_cod+line.c)/(line.a**2 + line.b**2)**0.5)
    
p1=Point(0,0)
print(p1)

p2=Point(1,1)
print(p2)

print(p1.euclidean_distance(p2))

print(p2.distance_origin())

li=Line(2,34,54)
print(li)

print(li.point_on_line_check(p1))

print(li.dist_point_line(p1))
