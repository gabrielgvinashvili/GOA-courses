from turtle import *

#we want to point a haus
speed(1)
#steo 1: draw a square
width(7)
color("purple")
forward(200)
left(90)
        
forward(200)    
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squar

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50,70)
pendown()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40) 

penup()
goto(150,70)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40) 

exitonclick() 