T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    print(f'#{test_case}',end = ' ')
    
    def recur(now):
        if now == N:
            print(now, end=' ')
            return
    
        print(now, end = ' ') # 호출 전
        recur(now+1) # 호출
        print(now, end=' ') # 호출하고 돌아와서 할 것
    recur(1)
    print()
