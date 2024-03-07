import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Cabeza_Raúl:
    def __init__(self, posx, flechitas):
        self.posx = posx
        self.posy = 240
        self.flechitas = flechitas
        self.vel = 0

    def draw(self):
        arcade.draw_lrtb_rectangle_filled(self.posx - 5, self.posx + 5, self.posy + 20, self.posy - 20, arcade.color.BLACK)

    def update(self):
        self.posy += self.vel
    def getPosy(self):
        return self.posy

class Ball:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.velx = 4
        self.vely = 4
        self.nueva_x = 0
        self.nueva_y = 0

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y,10, arcade.color.BLUE)
    def update(self, pos1, pos2):
        self.nueva_x = self.position_x + self.velx
        self.nueva_y = self.position_y + self.vely

        if self.nueva_x >= 600 and (pos1 + 100 >= self.nueva_y >= pos1 - 100) or self.nueva_x <= 40 and (pos2 + 100 >= self.nueva_y >= pos2 - 100):
            self.velx *= -1
            self.nueva_x = self.position_x + self.velx
        if self.nueva_y >= SCREEN_HEIGHT - 10 or self.nueva_y <= 10:
            self.vely *= -1
            self.nueva_y = self.position_y + self.vely

        self.position_x = self.nueva_x
        self.position_y = self.nueva_y



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50)
        self.p1 = Cabeza_Raúl(30, False)
        self.p2 = Cabeza_Raúl(610, True)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.p1.draw()
        self.p2.draw()

    def update(self, delta_time):
        pos1 = self.p1.getPosy()
        pos2 = self.p2.getPosy()
        print(pos1, pos2)
        self.ball.update(pos1, pos2)
        self.p1.update()
        self.p2.update()

    def on_key_press(self, key, modifiers):
        """ Called to update our objects.
        Happens approximately 60 times per second."""

        if key == arcade.key.W:
            self.p1.vel = 4
        elif key == arcade.key.S:
            self.p1.vel = -4
        if key == arcade.key.DOWN:
            self.p2.vel = -4
        elif key == arcade.key.UP:
            self.p2.vel = 4
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.p1.vel = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.p2.vel = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()