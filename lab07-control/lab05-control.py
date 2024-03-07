""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Moñeco:
    def __init__(self, posx, posy, color):
        self.posx = posx
        self.posy = posy
        self.color = color
        # Snow
        arcade.draw_circle_filled(0, 0, 60, [255, 255, 255])
        arcade.draw_circle_filled(0, 80, 50, [255, 255, 255])
        arcade.draw_circle_filled(0, 140, 40, [255, 255, 255])
        # Eyes
        arcade.draw_circle_filled(15, 150, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(15, 150, 5, arcade.color.BLACK)

    def dibujar(self):
        """ Draw a snow person """
        # Snow
        arcade.draw_circle_filled(self.posx, self.posy, 60, [255, 255, 255])
        arcade.draw_circle_filled(self.posx, self.posy + 80, 50, [255, 255, 255])
        arcade.draw_circle_filled(self.posx, self.posy + 140, 40, [255, 255, 255])

        # Eyes
        arcade.draw_circle_filled(self.posx + 15, self.posy + 150, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.posx - 15, self.posy + 150, 5, arcade.color.BLACK)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        """ Draw a snow person """
        # Snow
        arcade.draw_circle_filled(0, 0, 60, [255, 255, 255])
        arcade.draw_circle_filled(0, 80, 50, [255, 255, 255])
        arcade.draw_circle_filled(0, 140, 40, [255, 255, 255])

        # Eyes
        arcade.draw_circle_filled(self.posx + 15, self.posy + 150, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.posx - 15, self.posy + 150, 5, arcade.color.BLACK)

        """"Creo al objeto moñeco"""
        self.moñeco = Moñeco()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BLUE)
        moñeco()

    def on_mouse_motion(self, x, y, dx, dy):



def main():
    window = MyGame()
    arcade.run()


main()