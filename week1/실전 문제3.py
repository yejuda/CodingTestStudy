# n과 k값 입력 받기
n, k = map(int, input("N과 K값을 입력하세요.(공백으로 구분): ").split())

# 횟수를 저장할 변수
num = 0

while True:
    # n이 1이 되면 반복문 종료
    if n == 1:
        break
    # n을 k로 나누었을 때, 나누어떨어진다면
    elif n % k == 0:
        # 몫 값을 n에 저장(n값 업데이트)
        n = n // k
        num += 1
    else:
        # n값에서 1을 뺀다
        n -= 1
        num += 1

print(f"최소 횟수는 {num}번 입니다.")
