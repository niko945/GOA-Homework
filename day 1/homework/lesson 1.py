from turtle import *


#we want to paint a house

#step1:draw a squere

width(7)
speed(5)
color("red")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(100)  #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(199)
end_fill()

penup()
goto(110, 110)
pendown()

color("brown")
begin_fill()
left(120)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
end_fill()


penup()
goto(20,110)
pendown()

begin_fill()
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
end_fill()



exitonclick()