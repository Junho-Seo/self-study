## 1437. 변수를 활용한 연산자 lv5

# 변수를 사용하지 않고 정수와 연산자만을 사용하여 요구사항을
# 충족하는 표현식을 작성하고 결과를 출력하시오
# 그 후, 변수를 사용하여 동일한 요구사항을 충족하도록
# 표현식을 작성하고 결과를 출력하시오

print(3*2)
print(3**2)
print((3**2)//(3*2))
print((3**2)%(3*2))
print((3**2)+((-3)**2))
print()

a=3
b=2
c=-3

mult = a*b
sqr = a**b
quo = sqr//mult
rem = sqr%mult
last = sqr+c**b

print(mult)
print(sqr)
print(quo)
print(rem)
print(last)