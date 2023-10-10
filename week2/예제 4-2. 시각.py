# 시각 입력받기
n = int(input("시각을 입력해주세요: "))
# 횟수 저장할 변수
count = 0

for i in range(n+1):  # 0부터 n까지
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(f"3이 포함된 횟수는 {count}회 입니다.")


## result
# 시각을 입력해주세요: 5
# 3이 포함된 횟수는 11475회 입니다.
