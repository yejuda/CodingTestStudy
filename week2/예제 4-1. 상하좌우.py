# 2부 chapter4. 구현

# N 입력받기
N = int(input())
planit = input().split()
x,y = 1,1

# 'L', 'R', 'U', 'D'에 따른 이동방향
move_plan = ['L', 'R', 'U', 'D']
xd = [0,0,-1,1]
yd = [-1,1,0,0]

# 이동계획을 하나씩 확인
for plan in planit:
    # 이동 후 좌표 구하기
    for i in range(len(move_plan)):
        if plan == move_plan[i]:
            xx = x + xd[i]
            yy = y + yd[i]
    # 공간을 벗어나는 경우 무시        
    if xx < 1 or yy < 1 or xx > N or yy > N:
        continue
        
    # 이동수행
    x, y = xx, yy

print(x,y)

## 출력
# 5
# R R R U D D
# 3 4
