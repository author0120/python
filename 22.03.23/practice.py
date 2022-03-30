import turtle as t

t.bgcolor("black")
t.color("yellow")
t.speed(0)

for x in range(50, 250, 10):

    for y in range(4):
        t.forward(x)
        t.left(90)

    t.left(15)
    t.forward(20)
