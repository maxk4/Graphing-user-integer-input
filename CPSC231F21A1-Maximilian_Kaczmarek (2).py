#Instructor name: Jonathan Hudson
#Student Name: Maximilian Kaczmarek
#Student Number: 30151219
#Date: 2021-09-20
#Tutorial: 07
#Program draws an x and y axis, with certain objects, and calculates intercepts based on user input

#import turtle
import turtle

#import math
import math

#constants
WIDTH = 800
HEIGHT = 600

#Getting Input
#xc and yc and radius is for the circle
#x1,y1,x2,y2 is for the line
xc = int(input("Enter circle x coordinate:"))

yc = int(input("Enter circle y coordinate:"))

radius = float(input("Enter radius of circle:"))

x1 = int(input("Enter line start x coordinate:"))

y1 = int(input("Enter line start y coordinate:"))

x2 = int(input("Enter line end x coordinate:"))

y2 = int(input("Enter line end y coordinate:"))

#setup turtle
pointer = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()
screen.delay(delay=0)

#drawing the x-axis and y-axis
turtle.penup()
turtle.forward(400)
turtle.pendown()
turtle.left(90)
turtle.forward(800)

pointer.penup()
pointer.setposition(0,300)
pointer.pendown()
pointer.forward(800)

#drawing the circle
pointer.penup()
pointer.setposition(xc,yc - radius)
pointer.color("red")
pointer.pendown()
pointer.circle(radius)

#drawing the line that intercepts the circle
pointer.penup()
pointer.setposition(x1,y1)
pointer.color("blue")
pointer.pendown()
pointer.setposition(x2,y2)
pointer.penup()

#Analytical Geometry for Intersection
a = ((x2 - x1)**2) + ((y2 - y1)**2)
b = 2 * (((x1- xc)*(x2-x1)) + ((y1-yc)*(y2-y1)))
c = ((x1 - xc)**2) + ((y1 - yc)**2) - (radius**2)


#The epsilon, where the unique case which is not a line, but a single point
if x1 == x2 and y1 == y2:
    distance = math.sqrt((xc - x1)**2 + (yc-y1)**2)
    epsilon = 0.75
    if radius - epsilon <= distance <= radius + epsilon:
        pointer.penup()
        pointer.setposition(x1,y1-5)
        pointer.color("green")
        pointer.pendown()
        pointer.circle(5)

    else:
        pointer.penup()
        pointer.setposition(400 - 39,300)
        pointer.color("green")
        pointer.write("No Intersect!")


#No intersection:
elif (b**2) - (4*a*c) < 0:
    pointer.penup()
    pointer.setposition(400 - 39,300)
    pointer.color("green")
    pointer.write("No Intersect!")


#One intersection
elif (b**2) - (4*a*c) == 0:
    pointer.penup()
    pointer.setposition(400 - 39,300)
    pointer.color("green")


#The intersecting circle for one intersection(math and drawing):
    alpha = (-b-math.sqrt((b**2) - (4*a*c)))/(2*a)
    if alpha >= 0 and alpha <= 1:
        x = (((1-alpha)*x1) + (alpha*x2))
        y = (((1-alpha)*y1) + (alpha*y2))

        pointer.penup()
        pointer.setposition(x,y-5)
        pointer.pendown()
        pointer.circle(5)

#Two intersections:
elif (b**2) - (4*a*c) > 0:
    pointer.penup()
    pointer.setposition(400 - 39,300)
    pointer.color("green")


#The first intersecting circle for two intersections(math and drawing):
    alpha1 = (-b-math.sqrt((b**2) - (4*a*c)))/(2*a)
    alpha2 = (-b+math.sqrt((b**2) - (4*a*c)))/(2*a)
    if alpha1 >= 0 and alpha1 <= 1:
        xnegative = (((1-alpha1)*x1) + (alpha1*x2))
        ynegative = (((1-alpha1)*y1) + (alpha1*y2))

        pointer.penup()
        pointer.setposition(xnegative,ynegative-5)
        pointer.color("green")
        pointer.pendown()
        pointer.circle(5)

#The second intersecting circle for two intersections(math and drawing):
    if alpha2 >= 0 and alpha2 <= 1:
        xpositive = (((1-alpha2)*x1) + (alpha2*x2))
        ypositive = (((1-alpha2)*y1) + (alpha2*y2))

        pointer.penup()
        pointer.setposition(xpositive,ypositive-5)
        pointer.color("green")
        pointer.pendown()
        pointer.circle(5)

#Bonus Loop
while True:
    x1_while = input("x1")
    try:
        x1_while = int(x1_while)

    except:
        print("All done")
        break


    y1_while = input("y1")
    try:
        y1_while = int(y1_while)

    except:
        print("All done")
        break

    x2_while = input("x2")
    try:
        x2_while = int(x2_while)
    except:
        print("All done")
        break

    y2_while = input("y2")
    try:
        y2_while = int(y2_while)
    except:
        print("All done")
        break

    pointer.penup()
    pointer.setposition(x1_while, y1_while)
    pointer.pendown()
    pointer.setposition(x2_while, y2_while)


#Exits the program after clicking on it
screen.exitonclick()

