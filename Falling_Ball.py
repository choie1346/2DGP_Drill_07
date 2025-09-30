from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

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