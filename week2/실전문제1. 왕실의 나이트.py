# 경우의 수 
count = 0

# 좌표 입력받기
dot = list(input())         # c2

# 좌표 변환(ASCII코드 활용)
dotx = int(dot[1])          # 2
doty= ord(dot[0]) - 96      # 3

# 이동 수
dx = [-2,-2,2,2,1,1,-1,-1]
dy = [-1,1,-1,1,-2,2,-2,2]

# 이동 후 좌표 구하기
for i in range(len(dx)):
    nx = dotx + dx[i]
    ny = doty + dy[i]
    
    # 범위를 벗어나는 경우 무시(1보다 작거나 8보다 큰 좌표는 존재하지 X)
    if nx>8 or ny>8 or nx<1 or ny<1 :
        continue
    count += 1

print(count)   # 6

## result
# c2
# 6
