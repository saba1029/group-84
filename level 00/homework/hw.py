from turtle import *

shape("turtle")

speed(30)
width(7)
color("purple")

begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
color("purple")
forward(200)
left(90)
forward(200)

left(90)
forward(120)
color("brown")
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)

exitonclick()