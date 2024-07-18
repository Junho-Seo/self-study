# %%
# 표준출력
# print()

text = "Hello, World!"
print(text)

#여러줄 입력
text = "Hello, World!\nMy name is seolmuah"

text = """Hello, World!
My name is seolmuah"""

text = '''Hello, World!
My name is seolmuah'''

print(text)
# %%
# 문자열에 변수 값을 넣는 방법
name = '홍길동'
age = 20

#(1) F-string (F-포맷팅)
text = f"이름:{name}, 나이:{age}"
print(text) #이름:홍길동, 나이:20
# %%
#표현식 처리 가능
text = f"이름:{name+'님'}, 나이:{age+5}"
print(text) #이름:홍길동님, 나이:25

#%%
#자릿수 지정
text = f"이름:{name:10}, 나이:{age:10}"
print(text) 
#이름:홍길동       , 나이:        20

text = f"이름:{name:2}, 나이:{age:2}"
print(text) #이름:홍길동, 나이:20

#정렬
# <:왼쪽정렬, ^:가운데정렬, >:오른쪽정렬
text = f"이름:{name:^10}, 나이:{age:^10}"
print(text) 
#이름:   홍길동    , 나이:    20    

text = f"이름:{name:>10}, 나이:{age:>10}"
print(text) 
#이름:       홍길동, 나이:        20


text = f"이름:{name:<10}, 나이:{age:<10}"
print(text)
#이름:홍길동       , 나이:20        
#%%
#자릿수를 다른 문자열로 지정
text = f"이름:{name:-^10}, 나이:{age:a^10}"
print(text) 
#이름:---홍길동----, 나이:aaaa20aaaa

#%%
print('안녕')
print('반갑습니다.')
# 안녕
# 반갑습니다.

print('안녕', end='지은,')
print('반갑습니다.')
# 안녕지은,반갑습니다.

print('사과', '포도', '귤')
#사과 포도 귤

print('사과', '포도', '귤', sep='-')
#사과-포도-귤
#%%
#표준 입력
#input() : 키보드로부터 입력을 받아서 문자열로 반환

print("이름을 입력하세요.")
text = input() 
print(text) #혜경

#%%
text = input("이름을 입력하세요.") 
print(text) #혜경

#%%
num = input("정수를 입력하세요") #10을 키보드로 입력
num = int(num) * 10 + 4
print(num) #104

# %%
num = int(input("정수를 입력하세요")) 
num = num * 10 + 4
print(num) #104

#%%
#실습
#섭씨온도 -> 화씨온도 바꿔서 출력
#공식 : 화씨온도 = 섭씨온도*1.8 + 32
celcius = float(input("섭씨온도를 입력하세요>"))
fahrenheit = celcius * 1.8 + 32
print(f"섭씨온도:{celcius}=>화씨온도:{fahrenheit}")
#섭씨온도:27.3=>화씨온도:81.14


print(f"섭씨온도:{celcius:<.1f}=>화씨온도:{fahrenheit:<.3f}")
#섭씨온도:27.3=>화씨온도:81.140

print(f"섭씨온도:{celcius:<10.1f}=>화씨온도:{fahrenheit:<10.3f}")
#섭씨온도:27.3      =>화씨온도:81.140 
# %%
#시퀀스 자료형 : 리스트, 튜플, 문자열 (정렬 o)
#Non-시퀀스 자료형 : 딕셔너리, 셋 (정렬 x)

#차이점 : 순서의 유무
#공통점 : 데이터를 담는 데이터 타입 (컬렉션, 컨테이너)

#%%
#논리 연산자
#(1) and : 모두 참이여야 참, 하나라도 거짓이면 거짓
#(2) or : 하나라도 참이면 참, 모두 거짓이면 거짓
#(3) not : 논리의 반전

#조건문의 조건식을 결합할때 쓰인다

#1) and (&:비트 and연산)
print(True and True) #True
print(True and False) #False
print(True & True) #True
print(True & False) #

#2) or (|: 비트 or연산)
print(True or True)  #True
print(True or False) #True 
print(False or False) #False
print(True | True) 
print(True | False) 
print(False | False) 

#3) not
print(not True) #False
print(not False) #True

#4) xor (배타논리합, ^)
# 다르면 True, 같으면 False
# print(True xor True) 
print(True ^ True) #False
print(False ^ False) #False
print(True ^ False) #True
print(False ^ True) #True

# %%
# 내림, 반올림, 올림
num = 3.3

#1) 내림
floor_num = int(num) #3 (int)
floor_num = num // 1 #3.0 (float)
print(floor_num)

#2) 반올림
round_num = round(num)
print(round_num) #3

round_num = round(num, 1) #소숫점 첫째짜리표시 (둘째자리 반올림)
print(round_num) #3.3

num = 1235
round_num = round(num, -1) 
print(round_num) #1240

#3) 올림
num = 3.3
# ceil_num = num // 1 + 1 #4
ceil_num = int(num + 0.99999999999999999999)
print(ceil_num) #4

#True==1, False==0
ceil_num = int(num) + (num != int(num)) 
print(ceil_num) #4


ceil_num = -(-num//1) #-(-4)
print(ceil_num) #4.0


ceil_num = (10//3) #3
ceil_num = -(-10//3) #-(-4)
print(ceil_num) #4.0

import math
ceil_num = math.ceil(num)
print(ceil_num)