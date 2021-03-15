"""
This program creates a beautiful sunset over an ocean.
It does this using graphical functions from the arcade library.
"""
#Set up
import arcade
import math
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

    #Draw the Boats
    for boat in boat_list:
        boat.draw_boat()
        boat.move_step()

    #Draw the Dolphins
    for dolphin in dolphin_list:
        dolphin.draw_dolphin()
        dolphin.move_step()

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

class Dolphin:
    """The dolphin class"""
    def __init__(self, start_x, start_y, velocity_x, velocity_y, scale):
        self.x = start_x
        self.y = start_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.scale = scale
        self.angle = 0
        self.sprite = arcade.Sprite("dolphin.png",0.25*self.scale)

    def move_step(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y
        self.angle += self.velocity_x*0.013
        if self.angle >= 360:
            self.angle = 0

    def draw_dolphin(self):
        """Draws this boat centered on x and y"""
        # Draw Dolphin
        #arcade.draw_ellipse_filled(self.x + math.sin(self.angle)*100, self.y+ math.cos(self.angle)*100, 150, 30, arcade.color.ASH_GREY, tilt_angle = self.angle)
        self.sprite.center_x = self.x + math.sin(self.angle)*100*self.scale
        self.sprite.center_y = self.y + math.cos(self.angle)*100*self.scale
        self.sprite.draw()
        arcade.draw_rectangle_filled(self.x,self.y-70*self.scale,400*self.scale,200*self.scale,arcade.color.BLUE_YONDER)
        # Draw a point at x, y for reference
        # arcade.draw_point(self.x , self.y, arcade.color.RED, 5)

def main():
    #Open window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Sunset")
    arcade.set_background_color(arcade.color.BLUE_YONDER)

    #Create some boats
    global boat_list
    boat_list = []
    boat_list.append(Boat(400, 200, arcade.color.PUCE, 1, 0, 0.5))
    boat_list.append(Boat(300, 100, arcade.color.RUSSET, 0.5, 0, 1))
    boat_list.append(Boat(470, 30, arcade.color.RUST, 1.7, 0, 0.7))

    #Make some dolphins
    global dolphin_list
    dolphin_list = []
    dolphin_list.append(Dolphin(10, 70, 2, 0, 0.7))
    dolphin_list.append(Dolphin(120, 70, 2, 0, 0.7))


    #Finish
    arcade.schedule(on_draw, 1/60)

    arcade.run()

if __name__ == "__main__":
    main()