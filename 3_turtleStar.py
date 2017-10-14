# draw a star with turtle
import turtle
t = turtle.Turtle()
disp = turtle.Screen()
# drw with black line and fill with yellow
t.color("black","yellow")
t.begin_fill()
while 1:
	t.forward(100)
	# turn left 190 degree
	t.left(190)
	# t.pos() return the coordinates of the turtle
	if abs(t.pos()) < 1:
		break
t.end_fill()
disp.exitonclick()
