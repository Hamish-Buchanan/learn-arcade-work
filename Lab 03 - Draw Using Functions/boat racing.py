"""
This program creates a beautiful sunset over an ocean.
It does this using graphical functions from the arcade library.
"""
#Set up
import arcade
import random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_star(center_x,center_y):
    """Draws a star centered on x and y"""
    arcade.draw_triangle_filled(center_x,center_y+15 ,center_x-5,center_y, center_x+5,center_y, arcade.color.SILVER_CHALICE)
    arcade.draw_triangle_filled(center_x,center_y-15 ,center_x-5,center_y, center_x+5,center_y, arcade.color.SILVER_CHALICE)
    arcade.draw_triangle_filled(center_x+15,center_y ,center_x,center_y+5, center_x,center_y-5, arcade.color.SILVER_CHALICE)
    arcade.draw_triangle_filled(center_x-15,center_y ,center_x,center_y+5, center_x,center_y-5, arcade.color.SILVER_CHALICE)

def draw_sunset(SCREEN_WIDTH,SCREEN_HEIGHT):
    """Draws sunset background"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH-1, SCREEN_HEIGHT-1, SCREEN_HEIGHT/2, arcade.color.RUSSIAN_VIOLET)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH-1, SCREEN_HEIGHT-2*(SCREEN_HEIGHT/12), SCREEN_HEIGHT/2, arcade.color.RUFOUS)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH-1, SCREEN_HEIGHT-3*(SCREEN_HEIGHT/12), SCREEN_HEIGHT/2, arcade.color.RUST)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH-1, SCREEN_HEIGHT-4*(SCREEN_HEIGHT/12), SCREEN_HEIGHT/2, arcade.color.ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH-1, SCREEN_HEIGHT-5*(SCREEN_HEIGHT/12), SCREEN_HEIGHT/2, arcade.color.SELECTIVE_YELLOW)
    arcade.draw_arc_filled(center_y=SCREEN_HEIGHT/2, center_x=SCREEN_WIDTH/2, width=4*(SCREEN_WIDTH/30), height=3*(SCREEN_HEIGHT/30), color=arcade.color.ORANGE_RED, start_angle=0, end_angle=180)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()
    #Draw Sky
    draw_sunset(SCREEN_WIDTH,SCREEN_HEIGHT)

    #Draw Stars
    draw_star(497,520)
    draw_star(9,570)
    draw_star(342,508)
    draw_star(485,585)
    draw_star(243,556)
    draw_star(167,570)
    draw_star(70,520)
    for boat in boat_list:
        boat.draw_boat()
        boat.move_step()

class Boat:
    """The boat class"""
    def __init__(self, start_x, start_y, color, velocity_x, velocity_y, scale):
        self.x = start_x
        self.y = start_y
        self.color = color
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.scale = scale

    def move_step(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def draw_boat(self):
        """Draws this boat centered on x and y"""
        # Draw boat base
        arcade.draw_triangle_filled(self.x - 100 * self.scale, self.y + 80 * self.scale, self.x - 100 * self.scale, self.y, self.x - 160 * self.scale,
                                    self.y + 80 * self.scale, self.color)
        arcade.draw_triangle_filled(self.x + 100 * self.scale, self.y + 80 * self.scale, self.x + 100 * self.scale, self.y, self.x + 160 * self.scale,
                                    self.y + 80 * self.scale, self.color)
        arcade.draw_lrtb_rectangle_filled(self.x - 100 * self.scale, self.x + 100 * self.scale, self.y + 80 * self.scale, self.y, self.color)
        # Draw mast and sail
        arcade.draw_lrtb_rectangle_filled(self.x - 10 * self.scale, self.x + 10 * self.scale, self.y + 220 * self.scale, self.y + 80 * self.scale, self.color)
        arcade.draw_triangle_filled(self.x, self.y + 220 * self.scale, self.x, self.y + 130 * self.scale, self.x + 80 * self.scale, self.y + 130 * self.scale,
                                    arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(self.x, self.x + 80 * self.scale, self.y + 130 * self.scale, self.y + 125 * self.scale, self.color)
        # Draw a point at x, y for reference
        # arcade.draw_point(x, y, arcade.color.RED, 5)

def main():
    #Open window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Sunset")
    arcade.set_background_color(arcade.color.BLUE_YONDER)

    #Create some boats
    boat_colors = [arcade.color.RED,arcade.color.ORANGE,arcade.color.YELLOW,arcade.color.GREEN,arcade.color.BLUE,arcade.color.PURPLE,arcade.color.INDIGO,arcade.color.VIOLET]
    global boat_list
    boat_list = []
    for i in range(len(boat_colors)):
        boat_list.append(Boat(0, 260-35*i, boat_colors[i], (random.randint(3,9)/10)**2, 0, 0.3))


    #Finish
    arcade.schedule(on_draw, 1/60)

    arcade.run()

if __name__ == "__main__":
    main()