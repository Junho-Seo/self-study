## 2997. 문자열과 리스트 메서드 3 lv3

def restructure_word(word, arr):
    for char in word:
        if char.isdecimal():
            for char in range(int(char)):
                if arr:  # arr가 비어있지 않은 경우에만 pop을 수행합니다.
                    arr.pop()
        else:
            while char in arr:  # arr에 해당 문자가 있는 동안 계속 제거합니다.
                arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

# 문장에서 잘못된 내용을 제거하는 함수 restructure_word 함수를 작성한다.
#   인자로 넘겨받은 word 문자열을 순회하며 아래 조건에 맞춰 arr에서 불필요한 문자열을 제거한다.
#     만약 순회중인 문자열이 숫자라면, 해당 숫자만큼 반복하여 arr의 마지막 요소를 제거한다.
#       isdecimal 메서드와 pop 메서드를 활용한다.
#    그 외의 경우, arr에서 해당 문자열을 제거한다.
#       remove 메서드를 활용한다.
#     불필요한 문제를 제거한 arr를 반환한다.
# 함수 호출 결과를 result 변수에 담고 result를 출력한다.

arr.extend(original_word)
print(arr)

result = restructure_word(word, arr)
print(result)

print(''.join(result))


#%% 주석 포함
def restructure_word(word, arr):
    for char in word:
        if char.isdecimal():
            # 문자가 숫자인 경우, 해당 숫자만큼 반복하여 arr의 마지막 요소를 제거합니다.
            for char in range(int(char)):
                if arr:  # arr가 비어있지 않은 경우에만 pop을 수행합니다.
                    arr.pop()
        else:
            # 문자가 숫자가 아닌 경우, arr에서 해당 문자를 모두 제거합니다.
            while char in arr:  # arr에 해당 문자가 있는 동안 계속 제거합니다.
                arr.remove(char)
    return arr

# 원본 문자열을 변수에 저장합니다.
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# 수정할 문자열을 변수에 저장합니다.
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# original_word를 리스트로 변환하여 arr에 저장합니다.
arr = list(original_word)

# 문장에서 잘못된 내용을 제거하는 함수 호출
result = restructure_word(word, arr)
# 리스트를 문자열로 변환하여 출력합니다.
print(''.join(result))

# %%
a = [1, 2, 3]

if a:
    print(a)
# %%
