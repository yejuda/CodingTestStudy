# s가 0이면 더해주고, 0이 아니면 곱해주어 가장 큰 수를 출력하였다.

# 계산값 저장 변수
result = 1  # 0으로 하면 출력값은 0이 나옴

s = map(int, input("문자열 S를 입력하세요: "))

for i in s:
    if i == 0:
        result += i
    else:
        result *= i
        
print(result)

## result
# 문자열 S를 입력하세요: 567
# 210
