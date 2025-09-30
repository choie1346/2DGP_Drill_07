from pico2d import *
import random

def reset_world():
    pass


def update_world():
    pass

def render_world():
    clear_canvas()

    update_canvas()


open_canvas()

reset_world()
while True:

    update_world()

    render_world()

    delay(0.05)

close_canvas()