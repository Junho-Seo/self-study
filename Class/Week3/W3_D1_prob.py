#%%
N = 6
arr = [7, 2, 5, 3, 4, 1]

for i in range(N-3, 2, -1):# 각 구간의 끝 인덱스 i
    for j in range(i):  # 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]# 왼쪽 원소가 더 크면 교환

print(*arr)

#%%
T = input()
for tc in range(4, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]

    min_v = arr[0]
    for i in range(1, N):
        if min_v > arr[i]:
            min_v = arr[i]

# print(f'#{tc} {}')