## 3327. 신화 클래스 정의하기 lv2

class Myth:
    type_of_myth = 0
    def __init__(self, name):
        self.name = name
        Myth.type_of_myth += 1
        print(name)
    
    @staticmethod
    def description():
        return print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')
    
Myth('dangun')
Myth('greek & rome')
print(f'현재까지 생성된 신화 수: {Myth.type_of_myth}')
Myth.description()