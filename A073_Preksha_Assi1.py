import turtle
import easygui

def draw_square(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_triangle(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_concentric_circles(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
    t.circle(radius * 0.66)
    t.circle(radius * 0.33)

def draw_custom_star(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

options = ["Square", "Equilateral Triangle", "Concentric Circles", "Custom Star"]
shape = easygui.buttonbox("Select a shape:", choices=options)

size = easygui.integerbox("Enter size (50-250):", lowerbound=50, upperbound=250)
color = easygui.enterbox("Enter a fill color:")

t = turtle.Turtle()

if shape == "Square":
    draw_square(t, size, color)
elif shape == "Equilateral Triangle":
    draw_triangle(t, size, color)
elif shape == "Concentric Circles":
    draw_concentric_circles(t, size, color)
elif shape == "Custom Star":
    draw_custom_star(t, size, color)

easygui.msgbox("Drawing completed successfully!")
turtle.bye()