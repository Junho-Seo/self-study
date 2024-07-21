#%%
import requests
from pprint import pprint

def fetch_weather_data(lat, lon, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url).json()
    return response

dict_keys = print(response.keys())

def extract_data(weather_json):
    main = weather_json.get('main', {})
    weather_data = weather_json.get('weather', [])
    return {
        'main': main,
        'weather_data': weather_data
    }

if __name__ == "__main__":
    lat = 37.56
    lon = 126.97
    api_key = 'f3c91e30a2c9ad7700a90abfc782ac4b'

    weather_json = fetch_weather_data(lat, lon, api_key)
    extracted_data = extract_data(weather_json)
    pprint(extracted_data)


#%%
import requests
from pprint import pprint

# 날씨 데이터를 가져오는 함수
def fetch_weather_data(lat, lon, api_key):
    # API 요청 URL 생성
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    # API 요청
    response = requests.get(url)
    # HTTP 에러 발생 시 예외를 발생시킴
    response.raise_for_status()
    # JSON 형태로 응답 반환
    return response.json()

# 영어 키 값을 한글로 변환하는 함수
def translate_keys(data):
    # 키 값 변환 맵핑
    translation_map = {
        'feels_like': '체감온도',
        'humidity': '습도',
        'pressure': '기압',
        'temp': '온도',
        'temp_max': '최고온도',
        'temp_min': '최저온도',
        'description': '요약',
        'icon': '아이콘',
        'main': '핵심',
        'id': '식별자'
    }
    
    translated_data = {}
    # 데이터 딕셔너리의 각 키 값을 변환
    for key, value in data.items():
        translated_key = translation_map.get(key, key)  # 변환 맵핑에 존재하지 않으면 원래 키 값을 사용
        translated_data[translated_key] = value
    
    return translated_data

# API 응답에서 필요한 데이터를 추출하고 키 값을 변환하는 함수
def extract_data(weather_json):
    # 'main' 키에 해당하는 데이터 추출
    main = weather_json.get('main', {})
    # 'weather' 키에 해당하는 데이터 추출 (weather는 리스트 형태로 오기 때문에 리스트의 첫 번째 요소만 사용)
    weather_data = weather_json.get('weather', [{}])[0]
    
    # 키 값 변환
    translated_main = translate_keys(main)
    translated_weather_data = translate_keys(weather_data)
    
    # 변환된 데이터를 딕셔너리 형태로 반환
    return {
        '기본': translated_main,
        '날씨': translated_weather_data
    }

if __name__ == "__main__":
    lat = 37.56  # 위도
    lon = 126.97  # 경도
    api_key = 'f3c91e30a2c9ad7700a90abfc782ac4b'  # OpenWeatherMap API 키

    # 날씨 데이터 가져오기
    weather_json = fetch_weather_data(lat, lon, api_key)
    # 데이터 추출 및 키 값 변환
    extracted_data = extract_data(weather_json)
    # 결과 출력
    pprint(extracted_data)

#%%
import requests
from pprint import pprint

# 날씨 데이터를 가져오는 함수
def fetch_weather_data(lat, lon, api_key):
    # API 요청 URL 생성
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    # API 요청
    response = requests.get(url)
    # HTTP 에러 발생 시 예외를 발생시킴
    response.raise_for_status()
    # JSON 형태로 응답 반환
    return response.json()

# 영어 키 값을 한글로 변환하는 함수
def translate_keys(data):
    # 키 값 변환 맵핑
    translation_map = {
        'feels_like': '체감온도',
        'humidity': '습도',
        'pressure': '기압',
        'temp': '온도',
        'temp_max': '최고온도',
        'temp_min': '최저온도',
        'description': '요약',
        'icon': '아이콘',
        'main': '핵심',
        'id': '식별자'
    }
    
    translated_data = {}
    # 데이터 딕셔너리의 각 키 값을 변환
    for key, value in data.items():
        translated_key = translation_map.get(key, key)  # 변환 맵핑에 존재하지 않으면 원래 키 값을 사용
        translated_data[translated_key] = value
    
    return translated_data

# 켈빈 온도를 섭씨로 변환하는 함수
def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

# API 응답에서 필요한 데이터를 추출하고 키 값을 변환하는 함수
def extract_data(weather_json):
    # 'main' 키에 해당하는 데이터 추출
    main = weather_json.get('main', {})
    # 'weather' 키에 해당하는 데이터 추출 (리스트의 첫 번째 요소 사용)
    weather_data = weather_json.get('weather', [{}])[0]
    
    # 키 값 변환
    translated_main = translate_keys(main)
    translated_weather_data = translate_keys(weather_data)
    
    # 섭씨 온도 추가
    if '온도' in translated_main:
        translated_main['온도(섭씨)'] = kelvin_to_celsius(translated_main['온도'])
    if '체감온도' in translated_main:
        translated_main['체감온도(섭씨)'] = kelvin_to_celsius(translated_main['체감온도'])
    if '최저온도' in translated_main:
        translated_main['최저온도(섭씨)'] = kelvin_to_celsius(translated_main['최저온도'])
    if '최고온도' in translated_main:
        translated_main['최고온도(섭씨)'] = kelvin_to_celsius(translated_main['최고온도'])
    
    # 변환된 데이터를 딕셔너리 형태로 반환
    return {
        '기본': translated_main,
        '날씨': translated_weather_data
    }

if __name__ == "__main__":
    lat = 37.56  # 위도
    lon = 126.97  # 경도
    api_key = 'f3c91e30a2c9ad7700a90abfc782ac4b'  # OpenWeatherMap API 키

    # 날씨 데이터 가져오기
    weather_json = fetch_weather_data(lat, lon, api_key)
    # 데이터 추출 및 키 값 변환
    extracted_data = extract_data(weather_json)
    # 결과 출력
    pprint(extracted_data)


# %%
