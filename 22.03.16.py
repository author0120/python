import turtle as t

t.shape("turtle")
d=100

#삼각형 그리기
t.color("blue")
for x in range(3):
    t.forward(d)
    t.left(120)

#사각형 그리기
t.color("green")
for x in range(4):
    t.forward(d)
    t.left(90)

#원 그리기
t.color("black")
t.circle(d)

#오각형 그리기
t.color("red")
for x in range(5):
    t.forward(d)
    t.left(72)


#육각형 그리기
t.color("yellow")
for x in range(6):
    t.forward(d)
    t.left(60)


#팔각형 그리기
t.color("black")
for x in range(8):
    t.forward(d)
    t.left(45)
