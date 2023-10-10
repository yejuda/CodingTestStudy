def solution(foodtime, k):
    time = 0
    
    while True:
        for i in range(len(foodtime)):
            if time >= k:
                break 

            elif foodtime[i] == 0:
                foodtime[i+1] -= 1
                time += 1

            else:
                foodtime[i] -= 1
                time += 1
            print(foodtime)

        if time >= k:   # for 루프를 빠져나온 후 다시 한 번 검사
            break

    return foodtime[i-2]

## result
[2, 1, 2]
[2, 0, 2]
[2, 0, 1]
[1, 0, 1]
[1, 0, 0]
2
1





'''
time=0
k=5
foodtime = [3,1,2]
while True:
    for i in range(len(foodtime)):
        if time >= k:
            break 

        elif foodtime[i] == 0:
            foodtime[i+1] -= 1
            time += 1

        else:
            foodtime[i] -= 1
            time += 1
        print(foodtime)
            
    if time >= k:   # for 루프를 빠져나온 후 다시 한 번 검사
        break

print(i)
print(foodtime[i-2])
'''
