import turtle as t

n = 5 #오각형을 그립니다.(다른 값을 입력하면 다른 도형을 그립니다).
t.color("purple")
t.begin_fill() #색칠할 영역을 시작합니다
for x in range(n): # n 만큼 반복
    t.forward(50) #거북이고 50만큼 앞으로 이동
    t.left(360/n) #거북이가 360%n 만큼 왼쪽으로 회전
t.end_fill() #색칠할 영역 마무리 
