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

forward = [1,0]
depth = [0,1]
directions = {
        "forward": Vector(1, 0),
        "up": Vector(0, -1),
        "down": Vector(0, 1)
        }

pos = Vector()
aim = Vector()

with open("input.txt", 'r') as input:
    for l in input:
        words = l.split()
        direction = words[0]
        value = int(words[1])
        if (direction == "up" or  direction == "down"):
            aim = aim.plus(directions.get(words[0]).times(value))
        elif (direction == "forward"):
            pos = pos.plus(aim.times(value)).plus(directions.get(direction).times(value))

print(pos)
print(f'Result is pos {pos}: {pos.x * pos.y}')
