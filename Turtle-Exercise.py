import turtle
import math

def square(t, length):
    try:
        for i in range(4):
        	t.fd(length)
        	t.lt(90)
        print(t)
        turtle.mainloop()
    except Exception:
        print("Error!")


def polygon(t, length, n):
    try:
        for i in range(n):
        	t.fd(length)
        	t.lt(360 / n)
        print(t)
        turtle.mainloop()
    except Exception:
        print("Error!")


def circle(t, radius, n):
	"""Draws a circle with the given radius and n lines
	"""
	length = 2 * math.pi * radius / n
	polygon(t, length, n)


def arc(t, radius, angle, n):
	"""Draws an arc with the given radius and angle using n lines
	"""
	arc_length = 2 * math.pi * radius * angle / 360
	try:
		for i in range(n):
			t.fd(arc_length/n)
			t.lt(angle/n)
		print(t)
		turtle.mainloop()

	except Exception:
		print("Error!")



bob = turtle.Turtle()
arc(bob, 120, 234, 50)

