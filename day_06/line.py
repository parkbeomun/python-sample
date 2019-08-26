import turtle as t

angle = 89 #거북이가 왼쪽으로 회전할 각도 지정 
t.bgcolor("black") #배경색
t.color("yellow") #펜색
t.speed(0) #스피드
for x in range(200): 
    t.forward(x) #x만큼 앞으로 이동
    t.left(angle)  #거북이가 왼쪽으로 89도 회전
