min_n = 1

n = int(input("동전 개수 N을 입력하세요: "))
s = list(map(int, input("문자열 s를 입력하세요.(공백으로 구분): ").split()))

s.sort()  # 오름차순 정렬 ([9 3 2 1 1 ])

for i in s:
    if i <= min_n:   # i가 현재 최솟값보다 작으면
        min_n += i   # 최솟값 업데이트
    else:            # 아니면(i가 최솟값보다 크면), 반복문 빠져나오기
        break   
    
print(min_n)

## result
# 동전 개수 N을 입력하세요: 3
# 문자열 s를 입력하세요.(공백으로 구분): 3 5 7
# 1
