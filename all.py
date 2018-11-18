import turtle
from random import randint

class Snake():
    def __init__(self, shape:str="circle", color:str="green"):
        self.actor = turtle.Turtle()

        self.actor.up()
        self.actor.shape(shape)
        self.actor.color(color)
        #self.actor.ht()

        self.positions = [(0, 0)]
        self.stamps = []
        self.direction = (0, 0)

    def move(self):
        x, y = self.positions[0]
        print(self.direction)
        x += self.direction[0]*20
        y += self.direction[1]*20
        self.positions.insert(0, (x, y))
        self.positions.pop(-1)
        print(self.positions)

    def append_tail(self):
        tail = self.positions[-1]
        self.positions.append(tail)

    def die(self):
        pass

class Food():
    def __init__(self, shape:str="circle", color:str="yellow"):
        self.actor = turtle.Turtle()
        self.actor.up()
        self.actor.shape(shape)
        self.actor.color(color)
        self.actor.ht()

        self.position = (0, 0)

class KeyMapper():
    def __init__(self, screen:turtle.Screen, actor, speed=1):
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

class Manager():
    def __init__(self, screen_size:int=500,  border_size:int=50, shape:str="snake", background_color:str="black"):
        #setup the screen
        self.screen_size = screen_size
        self.border_size = border_size

        self.screen = turtle.Screen()
        self.screen.title(shape)
        self.screen.setup(screen_size + border_size, screen_size + border_size)
        self.screen.bgcolor(background_color)

        self.food = Food()
        self.snake = Snake()

        self.utils = Utils()
        self.stop = False

        self.start()

    def start(self):
        self.food.position = Utils.get_rand_position(self.screen_size)
        KeyMapper(self.screen, self.snake).map_the_key()
        self.update()
        turtle.mainloop()

    def display(self):
        tracer = self.screen.tracer()
        self.screen.tracer(0)

        self.food.actor.clearstamps(1)
        self.snake.actor.clearstamps(len(self.snake.positions))

        self.food.actor.goto(self.food.position[0], self.food.position[1])
        self.food.actor.stamp()

        for x, y in self.snake.positions:
            self.snake.actor.goto(x, y)
            self.snake.actor.stamp()

        self.screen.tracer(tracer)

    def draw_snake(self):
        self.snake.move()

        if self.check_collision_border() or self.check_collision_self():
            self.stop = True
        
        if self.check_collision_food():
            self.snake.append_tail()
            self.food.position = Utils.get_rand_position(self.screen_size)

    def update(self):
        if self.stop:
            self.gameover()
            return
            
        self.draw_snake()
        self.display()
        self.screen.ontimer(self.update, 100)

    def check_collision_food(self)-> bool:
        return Utils.get_distance(self.snake.positions[0], self.food.position) < 20

    def check_collision_self(self)-> bool:
        return len(set(self.snake.positions)) < len(self.snake.positions)

    def check_collision_border(self)-> bool:
        x, y = self.snake.positions[0]
        return not (-self.screen_size//2 - self.border_size < x <self.screen_size//2 + self.border_size) or \
               not (-self.screen_size//2 - self.border_size < y <self.screen_size//2 + self.border_size)

    def gameover(self):
        notification = turtle.Turtle()
        notification.up()
        notification.ht()
        notification.color("red")
        notification.write("GAME OVER\nScore : %04d" % (len(self.snake.positions)), align="center", font=("Arial", 30, "bold"))
        self.screen.onclick(lambda *a: [self.screen.bye(),exit()])

class Utils():
    @classmethod
    def get_rand_position(cls, size:int) -> int:
        return (randint(-size//2, size//2), randint(-size//2, size//2))

    @classmethod
    def get_distance(cls, pos_a:tuple, pos_b:tuple) -> float:
        return ( (pos_a[0]-pos_b[0])**2 + (pos_a[1]-pos_b[1])**2 ) ** 0.5

if __name__ == "__main__":
    manager = Manager()