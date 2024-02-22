import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(posy):
    """ Draw a snow person """
    R = random.randint(0,255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    posx = random.randint(100,700)
    # Snow
    arcade.draw_circle_filled(posx, posy, 60, [R,G,B])
    arcade.draw_circle_filled(posx, posy+80, 50, [R,G,B])
    arcade.draw_circle_filled(posx, posy+140, 40, [R,G,B])

    # Eyes
    arcade.draw_circle_filled(posx-15, posy+150, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(posx+15, posy+150, 5, arcade.color.BLACK)
def dibujar_manifestación():
    cantidad_muñecos = random.randint(1,7)
    tope_muñecos = cantidad_muñecos//6 + 1
    posy = 180
    for i in range(cantidad_muñecos):
        draw_snow_person(posy)
        if((i + 1) % tope_muñecos == 0):
            posy -= 20
def on_draw(delta_time):
    arcade.start_render()
    draw_grass()
    dibujar_manifestación()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    arcade.schedule(on_draw, 1/200)
    arcade.run()

# Call the main function to get the program started.
main()