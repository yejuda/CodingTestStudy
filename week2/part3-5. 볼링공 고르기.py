# 조합 문제
import itertools

n, m = map(int, input("볼링공 개수와 최대 무게 입력: ").split())
ball = list(map(int, input("공의 무게 볼링공 개수만큼 입력(공백으로 구분): ").split()))

# 볼링공 무게의 모든 조합 생성
combinations = list(itertools.combinations(ball, 2))

# 동일한 숫자로 이루어진 조합을 제외하고 넣을 빈 리스트
unique_ball = []

for combo in combinations:
    if combo[0] != combo[1]:      # 두 숫자가 같지 않다면
        unique_ball.append(combo)  # 빈 리스트에 붙이기
    else:  # 동일한 숫자로 이루어진 조합은 제외
        pass

print(unique_ball)
print(f"볼링공을 고르는 경우의 수는 {len(unique_ball)}가지 입니다.")

## result
# 볼링공 개수와 최대 무게 입력: 5 3
# 공의 무게 볼링공 개수만큼 입력(공백으로 구분): 1 3 2 3 2

# [(1, 3), (1, 2), (1, 3), (1, 2), (3, 2), (3, 2), (2, 3), (3, 2)]
# 볼링공을 고르는 경우의 수는 8가지 입니다.
