import turtle
import math

primes = []
nums = []
ulam_nums = []

def main():
    bound = int(input("Please input a positive integer."))

    for x in range(2, bound):
        nums.append(x)

    for x in range(1, bound):
        ulam_nums.append(x)
        ulam_nums.append(x)

    for i in range(2, bound):
        if is_prime(i):
            primes.append(i)

    print(primes)

    drawer()


def is_prime(num):
    square_root = int(math.ceil(math.sqrt(num)))
    for j in range(2, square_root+1):
        if (num % j is 0) and (num is j):
            continue
        elif (num % j is 0) and (num is not j):
            return False

    return True


def drawer():
    pensize = 2
    steps = 0
    index = 0

    prime_drawer_turtle = turtle.Turtle()
    prime_screen = turtle.Screen()
    prime_drawer_turtle.up()
    prime_drawer_turtle.speed(0)

    prime_screen.bgcolor("white")

    prime_drawer_turtle.dot(pensize, "orange")
    for j in nums:
        prime_drawer_turtle.forward(2)
        if j in primes:
            prime_drawer_turtle.dot(pensize, "blue")
        steps += 1

        if steps is ulam_nums[index]:
            prime_drawer_turtle.left(90)
            steps = 0
            index += 1

    prime_drawer_turtle.hideturtle()

    ts = prime_drawer_turtle.getscreen()
    canvas = ts.getcanvas()

    canvas.postscript(file="ulam.eps")

if __name__ == "__main__":
    main()

