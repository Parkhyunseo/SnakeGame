import turtle

from food import Food
from snake import Snake
from keymapper import KeyMapper
from utils import Utils

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