import turtle

class Snake():
    def __init__(self, shape:str="circle", color:str="green"):
        self.actor = turtle.Turtle()

        self.actor.up()
        self.actor.shape(shape)
        self.actor.color(color)
        self.actor.ht()

        self.positions = [(0, 0)]
        self.stamps = []
        self.direction = (0, 0)

    def move(self):
        x, y = self.positions[0]
        x += self.direction[0]*20
        y += self.direction[1]*20
        self.positions.insert(0, (x, y))
        self.positions.pop(-1)

    def append_tail(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def die(self):
        pass