## 1440. 메서드를 활용한 문자열 뒤집기 lv1

# 아래 함수를 수정하시오.
def reverse_string(rev):
    rev_list = list(rev)
    rev_list.reverse()
    rev_done = ''.join(rev_list)
    return rev_done

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
