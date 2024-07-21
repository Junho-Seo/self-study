import requests

def prob3():
    dummy_data = []
    for idx in range(1, 11):
        API_URL = f'https://jsonplaceholder.typicode.com/users/{idx}'
        response = requests.get(API_URL)
        parsed_data = response.json()
        dummy_dict = {}
        lat = float(parsed_data['address']['geo']['lat'])
        lng = float(parsed_data['address']['geo']['lng'])
        if lat <= -80 or lng <= -80 or lat >= 80 or lng >= 80:
            continue
        dummy_dict['name'] = parsed_data['name']
        dummy_dict['company'] = parsed_data['company']['name']
        dummy_dict['lat'] = lat
        dummy_dict['lng'] = lng
        dummy_data.append(dummy_dict)
    #print(dummy_data)
    return dummy_data

prob3()

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def censorship(user_info):
    company = user_info['company']
    name = user_info['name']
    if company in black_list:
        print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False
    else: #else 빼도 똑같음. 왜냐하면 뒤의 코드는 계속 실행되기 때문
        print('이상 없습니다.')
        return True

def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        company = user['company'] # key 값
        name = user['name'] # value 값 -> 나중에 리스트로 추가됨

        # 블랙리스트에 있다면 False가 반환. continue 해주면 된다.
        if censorship(user) is False:
            continue

        # 만약 이미 존재하는 회사라면, value 값을 append
        if company in censored_user_list:
            censored_user_list[company].append(name)
        # 없는 회사라면 key value 를 리스트 형태로 추가
        else:
            censored_user_list[company] = [name]
    
    return censored_user_list


def prob4():
    user_list = prob3()
    censored_user_list = create_user(user_list)
    print(censored_user_list)

prob4()