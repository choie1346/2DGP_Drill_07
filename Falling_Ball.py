from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Ball:
    def __init__(self):
        self.size = random.randint(1, 2) * 30
        if self.size == 30:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.x = random.randint(0, 800 - self.size)
        self.y = 599

    def update(self):
        if self.y > 40:
            y = self.y - 10
        else:
            y = 40
        self.y = y

    def draw(self):
        self.image.draw(self.x + self.size // 2, self.y + self.size // 2, self.size, self.size)

def reset_world():
    global grass
    grass = Grass()

    global balls
    balls = [Ball() for i in range(20)]


def update_world():
    for ball in balls:
        ball.update()

def render_world():
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
    update_canvas()


open_canvas()

reset_world()
while True:

    update_world()

    render_world()

    delay(0.05)

close_canvas()