class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def setx(self, x):
    self.x = x

def sety(self, y):
    self.y

def get(self):
    return self.x, self.y

def move(self, offsetx, offsety):
    self.x += offsetx
    self.y += offsety

def __repr__(self):
    print('(' + str(self.x) + ',' + str(self.y) + ')') 


p = Point()
p.setx(5)

