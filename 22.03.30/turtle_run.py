# 터틀런 만들기
# 거북이를 조종해서 도망치는 게임 만들기
# 악당 거북이를 피해서 도망쳐야 하며 초록색 동그라미를 최대한 많이 먹어야 함

import turtle as t
import random
from tkinter import*

# 악당 거북이 생성
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이 생성
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

#사용자 거북이의 동작 정의
def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

# 게임 플레이 코드
def play():
    t.forward(12)
    ang = te.towards(t.pos())
    te.setheading(ang)
    te.forward(8)

    if t.distance(ts) < 12:        
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)        
        ts.goto(star_x, star_y)        
    if t.distance(te) >= 12:
        t.ontimer(play, 100)
        

# 배경 설정
# 창 크키는 가로 세로 500, 배경색은 오랜지
t.setup(500, 500)
t.bgcolor("orange")

t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()


play()
