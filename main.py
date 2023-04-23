import random
# zee.forward(100)
# zee.right(90)
# zee.forward(100)
# zee.right(90)
# zee.forward(100)
# zee.right(90)
# zee.forward(100)
# zee.right(90)
# for _ in range(15):
#     zee.dot(20, 'white')
#     zee.forward(20)
#
# zee.right(90)
#
# for _ in range(10):
#     zee.forward(10)
#     zee.pendown()
#     zee.forward(10)
#     zee.penup()

# color = ['blue', 'green', 'yellow', 'red']
# n = 8
# s = 3
# while n > 0:
#     c = n % 4
#     zee.color(color[c])
#     for _ in range(s):
#         zee.forward(100)
#         zee.right(360/s)
#     s += 1
#     n -= 1


import turtle as t
import random

zee = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = (r, g, b)
    return a


# zee.pensize(15)
# zee.speed(0)
# for _ in range(200):
#     zee.color(random_color())
#     zee.forward(30)
#     zee.setheading(random.choice([0, 90, 180, 270]))

# src = Screen()
# src.exitonclick()
t.speed(0)
for _ in range(300):
    t.color(random_color())
    t.circle(100)
    t.left(360/300)
t.hideturtle()

src = t.Screen()
src.exitonclick()



