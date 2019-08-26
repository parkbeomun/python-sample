import turtle as t
n = 50 # 원을 50개 그림
t.bgcolor("black") # 배경색
t.color("green") # 펜색 
t.speed(0) # 거북이 속도 가장빠르게 설정
for x in range(n): # n번 반복
    t.circle(80) # 현재 위치에서 반지름이 80인 원을 그림 
    t.left(360/n) ## 거북이가 360/n 만큼 왼쪽으로 회전
