"""
This program creates a beautiful sunset over an ocean.
It does this using graphical functions from the arcade library.
"""
#Set up
import arcade
arcade.open_window(600, 600, "Sunset")
arcade.set_background_color(arcade.color.BLUE_YONDER)

def star(center_x,center_y):
    arcade.draw_triangle_filled(center_x,center_y+15 ,center_x-5,center_y, center_x+5,center_y, arcade.color.SILVER_CHALICE)
    arcade.draw_triangle_filled(center_x,center_y-15 ,center_x-5,center_y, center_x+5,center_y, arcade.color.SILVER_CHALICE)
    arcade.draw_triangle_filled(center_x+15,center_y ,center_x,center_y+5, center_x,center_y-5, arcade.color.SILVER_CHALICE)
    arcade.draw_triangle_filled(center_x-15,center_y ,center_x,center_y+5, center_x,center_y-5, arcade.color.SILVER_CHALICE)



#Drawing
arcade.start_render()
#Draw Sky
arcade.draw_lrtb_rectangle_filled(0, 599, 599, 300, arcade.color.RUSSIAN_VIOLET)
arcade.draw_lrtb_rectangle_filled(0, 599, 500, 300, arcade.color.RUFOUS)
arcade.draw_lrtb_rectangle_filled(0, 599, 450, 300, arcade.color.RUST)
arcade.draw_lrtb_rectangle_filled(0, 599, 400, 300, arcade.color.ORANGE)
arcade.draw_lrtb_rectangle_filled(0, 599, 350, 300, arcade.color.SELECTIVE_YELLOW)

#Draw Stars
star(497,520)
star(9,570)
star(342,508)
star(485,585)
star(243,556)
star(167,570)
star(70,520)

#Draw Sun
arcade.draw_arc_filled(center_y=300, center_x=300, width=90, height=60, color=arcade.color.ORANGE_RED, start_angle=0, end_angle=180)

#Draw Boat
arcade.draw_triangle_filled(200,130,200,50,140,130,arcade.color.RUSSET)
arcade.draw_triangle_filled(400,130,400,50,460,130,arcade.color.RUSSET)
arcade.draw_lrtb_rectangle_filled(200,400, 130, 50, arcade.color.RUSSET)
arcade.draw_lrtb_rectangle_filled(290,310, 270, 130, arcade.color.RUSSET)
arcade.draw_triangle_filled(290,270,290,180,380,180,arcade.color.WHITE)

arcade.finish_render()

#Finish
arcade.run()
