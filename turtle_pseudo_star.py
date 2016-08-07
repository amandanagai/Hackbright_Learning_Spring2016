import turtle
star = turtle.Turtle()

i = 0

while i < 3:
	star.forward(80)
	star.right(120)

	star.forward(80)
	star.right(120)

	star.forward(80)
	star.right(30)
	i += 1

while i <= 8:
	star.forward(80)
	star.right(120)

	star.forward(80)
	star.right(120)

	star.forward(80)
	star.right(45)
	i += 1
# star.right(30)

# star.forward(20)
# star.right(30)

# star.forward(20)
# star.right(30)

# star.forward(20)
# star.right(30)

turtle.done()

window.exitonclick()