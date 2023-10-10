num = int(input("모험가의 수 입력: "))
panic = list(map(int, input("모험가의 공포도 입력(모험가의 수 이하의 자연수로 입력하세요.: ").split()))
cnt = 0  # 현재 그룹에 포함된 모험가의 수
group = 0  # 그룹 수

panic.sort()  # 1 2 2 2 3

# 공포도의 수를 작은 것부터 확인하면서
for i in panic:
    cnt += 1
    if cnt == i:
        group += 1
        cnt = 0  # 현재 모험가 수 초기화
        
print(group)

## result
# 모험가의 수 입력: 5
# 모험가의 공포도 입력(모험가의 수 이하의 자연수로 입력하세요.: 2 3 1 2 2
# 2
