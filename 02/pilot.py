"""
This solution is over engineered for the fun of it. I know
"""
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)

    def plus(self, v):
        res = Vector()
        res.x = self.x + v.x
        res.y = self.y + v.y
        return res

    def times(self, value):
        res = Vector(self.x * value, self.y * value)
        return res

input = open("input.txt", 'r')
lines = input.readlines()

forward = [1,0]
depth = [0,1]
directions = {
        "forward": Vector(1, 0),
        "up": Vector(0, -1),
        "down": Vector(0, 1)
        }

pos = Vector()

for l in lines:
    words = l.split()
    direction = words[0]
    value = int(words[1])
    pos = pos.plus(directions.get(words[0]).times(value))

print(pos)
print("Result is pos {0}: {1}".format(pos, pos.x * pos.y))

input.close()
