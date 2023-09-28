# n은 배열의 크기
# m은 숫자가 더해지는 횟수
# k는 연속으로 더할 수 있는 횟수

n, m, k = map(int, input("n,m,k의 값을 입력하세요.(공백으로 구분): ").split())
list_num = list(map(int, input("n길이의 자연수를 입력하세요. (공백으로 구분): ").split()))


# 큰 수부터 정렬
list_num = sorted(list_num, reverse=True)
list_num


# k번까지 더하기 위해, 횟수 세는 변수
num = 0
# 최종 더한 값
last_sum = 0

# num이 숫자가 더해질 수 있는 횟수가 될 때까지 반복
while num < m:
    for i in range(k):
        last_sum += list_num[0]  # 0번 인덱스를 더해서 last_sum에 저장 (k만큼 반복)
        num += 1
    # 끝나면
    last_sum += list_num[1]
    num += 1

print(f"최종으로 더해진 가장 큰 수는 {last_sum}입니다.")
