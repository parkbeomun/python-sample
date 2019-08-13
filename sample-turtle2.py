#-*- coding:utf-8 -*-

import turtle as t

#삼각형 그리기
t.color("red") #펜 색상 빨간색으로 변경 
t.forward(100) #거북이가 100만큼 앞으로 이동합니다.
t.left(120) #거북이가 왼쪽으로 120도 회전합니다.
t.forward(100) # 위과정을 두번 반복합니다
t.left(120)
t.forward(100)
t.left(120)

#사각형 그리기
t.color("green") #펜 색상 초록색으로 변경
t.pensize(3) #펜 굵기 3으로  변경 
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

#원그리기
t.color("blue")
t.pensize(5) #펜 굵기 파란색으로 변경
t.circle(50) #반지름이 50인 원을 그립니다.
