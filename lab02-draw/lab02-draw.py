import arcade

arcade.open_window(1200, 800, "Dibujaciones insanas")
arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()
# Circulín
arcade.draw_circle_outline(600, 400, 100, arcade.color.WHITE, 5)
arcade.draw_circle_filled(550, 420, 6, arcade.color.WHITE, 5)
arcade.draw_circle_filled(650, 420, 6, arcade.color.WHITE, 5)
arcade.draw_arc_outline(600, 370, 50, 50, arcade.color.WHITE, 225, 315, 8)

arcade.draw_line(450, 500, 750, 500, arcade.color.GRAY, 6)
arcade.draw_line(470, 500, 470, 520, arcade.color.GRAY, 6)
arcade.draw_line(730, 500, 730, 520, arcade.color.GRAY, 6)

arcade.draw_circle_filled(457,530,6,arcade.color.WHITE)
arcade.draw_line(455, 520, 470, 518, arcade.color.WHITE, 3)
arcade.draw_line(455, 530, 455, 502, arcade.color.WHITE, 3)
arcade.draw_line(455, 502, 465, 492, arcade.color.WHITE, 3)
arcade.draw_line(465, 492, 465, 480, arcade.color.WHITE, 3)


arcade.draw_circle_filled(743,530,6,arcade.color.WHITE)
arcade.draw_line(730, 520, 745, 518, arcade.color.WHITE, 3)
arcade.draw_line(745, 530, 745, 502, arcade.color.WHITE, 3)
arcade.draw_line(745, 502, 735, 492, arcade.color.WHITE, 3)
arcade.draw_line(735, 492, 735, 480, arcade.color.WHITE, 3)




arcade.run()
