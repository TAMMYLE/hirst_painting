import colorgram
import turtle
import random

tim = turtle.Turtle()



extracted_colors = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), 
                    (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
                    (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), 
                    (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
                    (222, 140, 203), (68, 240, 161), (5, 38, 33), (68, 219, 155)]
turtle.colormode(255)
# extracting RGB colors from an image
""" for i in t_colors:

    extracted_color_red = i.rgb.r
    extracted_color_green = i.rgb.g
    extracted_color_blue = i.rgb.b

    extracted_color = (extracted_color_red, extracted_color_green, extracted_color_blue)

    extracted_colors.append(extracted_color)

print(extracted_colors) """

# main program requirements

""" 1. 10x10 rows of spots 
2. each spot size 20, space 50 in between """  

def straight_line():

    for space in range(10):
        tim.dot(20, random.choice(extracted_colors))
        tim.forward(50)

# start_x, start_y: starting coordinates for the turtle
# line_height: vertical distance between lines
# 'y' position is adjusted by adding line_height * i for each iteration to move turtle up

start_x = -250
start_y = -250
line_height = 50 

for i in range(10):
    tim.hideturtle()
    tim.penup()
    tim.setpos(start_x, start_y + line_height * i)
    tim.showturtle()
    straight_line()

# create new screen that can behave what we need
screen = turtle.Screen()
screen.exitonclick() 

