# 2996. 문자열과 리스트 메서드2 lv2

data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# data_1을 순회하며 대문자이거나 공백 ' '인 경우만 출력한다.
# 문자열 메서드 isupper를 활용한다.
# 모든 문자열은 한 줄에 출력되어야 한다.

for lne in data_1:
    if lne.isupper() == True or lne == ' ':
        print(lne, end='')


print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []

arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다'))
print(arr)

arr.sort()
print(arr)
# data_2에서 정렬된 arr을 순회하여 얻은 각 요소 번째에 위치한 문자열을 출력한다.
# 모든 문자열은 한 줄에 출력되어야 한다.

for i in arr:
    print((data_2[i]), end='')

# result = ''.join([data_2[i] for i in arr])
# print(result)