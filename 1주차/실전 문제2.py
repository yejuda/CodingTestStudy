import random

# 행과 열의 수 입력 받기
rows, cols = map(int,input("행의 수와 열의 수를 입력하세요.(공백으로 구분)").split())

# 1부터 100 사이의 랜덤한 배열 생성
# 외부 루프 실행 후 내부 루프 실행
random_arr = [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

# 각 행의 최댓값을 저장할 빈 리스트
min_list = []

# 행을 돌아가면서 max값 저장
for row in random_arr:
    print(row)


# 행을 돌아가면서 max값 저장
for row in random_arr:
    min_list.append(min(row))

print(max(min_list))
