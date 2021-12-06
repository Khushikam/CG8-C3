import turtle
length = 10
while length <= 150:
    for i in range(10):
        turtle.pencolor('red')
        turtle.backward(length)
        turtle.right(90)
        length += 5
        turtle.pencolor('green')
        turtle.forward(length)
        turtle.right(90)
        length += 5
