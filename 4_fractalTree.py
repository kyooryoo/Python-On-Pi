import turtle
import random

def fractal_tree(b_len, t):
	if b_len > 5:
		temp = random.randint(1, b_len)
		temp_angle = random.randint(1, 25)
		t.forward(temp)
		t.right(temp_angle)
		fractal_tree(b_len - 10, t)
		t.left(2 * temp_angle)
		fractal_tree(b_len - 10, t)
		t.right(temp_angle)
		t.backward(temp)

t = turtle.Turtle()
disp = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
fractal_tree(90, t)
disp.exitonclick()
