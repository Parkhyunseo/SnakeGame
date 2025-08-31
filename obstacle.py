import turtle

class Obstacle():
    def __init__(self, shape:str="circle", color:str="yellow"):
        self.actor = turtle.Turtle()
        self.actor.up()
        self.actor.shape(shape)
        self.actor.color(color)
        self.actor.ht()

        self.position = (0, 0)
        self.debugCode = 0