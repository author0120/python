# 키보드로 거북이 조종해서 그림 그리기
# 거북이가 방향을 바꿀 때마다 선의 색깔도 바뀌게 그리기
# Right는 빨간색, left는 파란색, down은 노란색, up은 보라색

import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)
    t.color("red")

def turn_up():
    t.setheading(90)
    t.forward(10)
    t.color("purple")

def turn_left():
    t.setheading(180)
    t.forward(10)
    t.color("blue")

def turn_down():
    t.setheading(270)
    t.forward(10)
    t.color("yellow")

def blank():
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.listen()
