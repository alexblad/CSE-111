# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from this import d
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the functions do draw things. 
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_sun(canvas, 700, 400, 500)
    draw_cloud(canvas, 100, 350, 450)
    draw_cloud(canvas, 325, 450, 500)
    draw_cloud(canvas, 300, 300, 375)
    draw_cloud(canvas, 550, 350, 450)
    for x in range(50,800, 50):
        draw_pine_tree(canvas, x, scene_height/3, 100)

    for x in range(0, 800,5):
        draw_fence(canvas, x, scene_height/10, 30)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")

def draw_cloud(canvas, center_x, bottom, height):

#draw cloud
    cloud_width=height
    cloud_height=height
    b_left_x=center_x - cloud_width/2
    b_left_y=height/1.4
    t_right_x= center_x + cloud_width/2
    t_right_y= height
    draw_oval(canvas,b_left_x, b_left_y, t_right_x, t_right_y, fill='ivory')

def draw_sun(canvas, center_x, bottom, height):
    #draw sun
    b_left_x=center_x - 75
    b_left_y=height/1.4
    t_right_x= center_x+75
    t_right_y= height
    draw_oval(canvas,b_left_x, b_left_y, t_right_x, t_right_y, fill='gold1')

def draw_pine_tree(canvas, center_x, bottom, height):
 
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the tree
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan4")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the skirt of the tree
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="forestGreen")

def draw_fence(canvas, center_x, bottom, height ):
    fence_width=height/12
    fence_height=height
    fence_b_left= center_x-fence_width
    fence_bottom=bottom
    fence_t_right=center_x+fence_width
    fence_top=height
    draw_rectangle(canvas, fence_b_left, fence_bottom, fence_t_right, fence_top, fill='chocolate3')
# Call the main function so that
# this program will start executing.
main()