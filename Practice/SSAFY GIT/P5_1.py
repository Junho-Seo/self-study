## 2995. 문자열과 리스트 메서드1 lv1

N = 9
data_1 = '123456789'
arr_1 = []
# N번만큼 반복하며 data_1에 담긴 문자열을
# 인덱스 번호 순서대로 arr_1 리스트에 추가
# append 메서드 활용하여 arr_1 리스트를 출력
for num in range(N):
    arr_1.append(data_1[num])

print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
arr_2 = data_2.split()
# data_2에 담긴 문자열을 공백을 기준으로 나누어 새로운 리스트 arr_2에 할당한다.
# 문자열 메서드 split을 활용한다.
# arr_2가 가진 요소들을 순회하여 홀수만 차례대로 출력한다.
for num in arr_2:
    if int(num) % 2 == 1:
        print(num)
