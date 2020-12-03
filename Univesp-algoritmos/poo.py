class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def setx(self,x):
        self.x = x
    def sety(self,y):
        self.y = y

    def get(self):
        return self.x, self.y
    def move(self,x,y):
        self.x += x
        self.y += y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

class Point3D(Point):
    def __init__(self):
        super().__init__()
        self.z = 0
    def setz(self,z):
        self.z = z
    def get(self):
        return self.x, self.y, self.z
    def move(self, x,y,z):
        super().move(x,y)
        self.z += z
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

p = Point()
p.setx(3)
p.sety(4)
p.move(1,2)
print(p)

q = Point()
q.setx(-1)
q.sety(2)
q.move(1,3)
x,y = q.get()
print(x,y)

r = Point3D()
r.setx(1)
r.sety(2)
r.setz(3)
r.move(1,1,1)
print(r)