import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.7
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Bueno(arcade.Sprite):
    def __init__(self):
        self.vely = random.randint(-1, 1)
        self.velx = random.randint(-1, 1)
        while self.vely == 0:
            self.vely = random.randint(-1, 1)
        while self.velx == 0:
            self.velx = random.randint(-1, 1)
    def update(self):
        b = 2

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")
        # Esconder cursor
        self.set_mouse_visible(False)

        # listas de seprites
        self.lista_jugador = None
        self.lista_malos = None
        self.lista_buenos = None

        # Data del juegador
        self.sprite = None
        self.puntos = 0

        arcade.set_background_color(arcade.color.WHITE)
    def setup(self):
        """Aquí se inicializan las variables jejeje"""
        # Espraits
        self.lista_jugador = arcade.SpriteList()
        self.lista_malos = arcade.SpriteList()
        self.lista_buenos = arcade.SpriteList()

        # puntos
        self.puntos = 0

        # poner en marcha al jugador
        self.sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", SPRITE_SCALING_PLAYER)
        self.sprite.center_x = 50
        self.sprite.center_y =50
        self.lista_jugador.append(self.sprite)

        # primera tanda de cosos buenos y cosos malos
        for i in range(21):
            bueno = arcade.Sprite(":resources:images/items/ladderTop.png", SPRITE_SCALING_COIN)

            bueno.center_y = random.randrange(SCREEN_HEIGHT)
            bueno.center_x = random.randrange(SCREEN_WIDTH)

            self.lista_buenos.append(bueno)




    def on_draw(self):
        arcade.start_render()
        self.lista_jugador.draw()
        self.lista_malos.draw()
        self.lista_buenos.draw()

    def on_update(self, delta_time: float):
        a = 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
