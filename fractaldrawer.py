import turtle
import random


def main():

    print("Enter Fractal size:")
    size = int(input())
    print("Enter duration (1000 to 10000):")
    duration = int(input())

    a = (0, size)
    b = (-size, 0)
    c = (size, 0)
    starting_point = (((0 + (-size))/2), ((size + 0)/2))

    drawer_turtle = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)
    drawer_turtle.up()
    pensize = 2

    drawer_turtle.goto(a)
    drawer_turtle.dot(5, "blue")
    drawer_turtle.goto(b)
    drawer_turtle.dot(5, "blue")
    drawer_turtle.goto(c)
    drawer_turtle.dot(5, "blue")


    drawer_turtle.goto(starting_point)

    for i in range(duration):
        value = random.randint(1, 6)
        x_state = drawer_turtle.xcor()
        y_state = drawer_turtle.ycor()

        if value == 1 or value == 2:
            go_coor_A = (((x_state + 0)/2), ((y_state + size)/2))
            drawer_turtle.goto(go_coor_A)
            drawer_turtle.dot(pensize, "blue")
        elif value == 3 or value == 4:
            go_coor_B = (((x_state + (-size))/2), ((y_state + 0)/2))
            drawer_turtle.goto(go_coor_B)
            drawer_turtle.dot(pensize, "blue")
        elif value == 5 or value == 6:
            go_coor_C = (((x_state + size)/2), ((y_state + 0)/2))
            drawer_turtle.goto(go_coor_C)
            drawer_turtle.dot(pensize, "blue")
        screen.update()

    drawer_turtle.hideturtle()

    ts = drawer_turtle.getscreen()
    canvas = ts.getcanvas()

    canvas.postscript(file="chaostri.eps")


if __name__ == "__main__":
    main()

