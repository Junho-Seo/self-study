T = int(input())

for tc in range(1, T+1):
    # 알고리즘 문제들
    # 입력 및 초기화
    # bucket은 tc마다 초기화가 되어야 한다.
    bucket = {
        'ssafy': 3,
        'bob': 5,
        'alice': 1,
        'giryun': 10,
        'hello': 0,
    }
    # 공백으로 구분되어있다? split 숫자면 map 추가
    people = input().split()
    for person in people:
        bucket[person] += 1
    # 따옴표 주의하기
    print(f"#{tc} {bucket['ssafy']}")



    #---------
    dict = {}
    #딕셔너리에서 key, value를 추가하는 방법
    dict['test'] = 3

    dict['smaple'] += 1 # 버그 발생
    # dict['sample'] = dict['sample'] + 1
    #                          |-> 없는 키값을 바로 조회하는 구간에서 버그가 발생한다.