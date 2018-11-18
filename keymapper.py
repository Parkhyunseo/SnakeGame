class KeyMapper():
    def __init__(self, screen, actor, speed=1):
        self.screen = screen
        self.actor = actor
        self.speed = speed

    def map_the_key(self):
        self.screen.onkeypress(self.up, "Up")
        self.screen.onkeypress(self.down, "Down")
        self.screen.onkeypress(self.right, "Right")
        self.screen.onkeypress(self.left, "Left")
        self.screen.listen()

    def right(self):
        self.set_direction(1, 0)

    def left(self):
        self.set_direction(-1, 0)

    def up(self):
        self.set_direction(0, 1)  
    
    def down(self):
        self.set_direction(0, -1)

    def set_direction(self, x, y):
        self.actor.direction = (x, y)