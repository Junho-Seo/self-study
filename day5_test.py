# #%%
# import requests

# url = 'https://fakestoreapi.com/carts'
# data = requests.get(url).json()
# print(data)

#%%
import requests
from pprint import pprint
# 서울의 위도 37.56 / 경도 126.97
lat = 37.56
lon = 126.97
api_key = 'f3c91e30a2c9ad7700a90abfc782ac4b'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
response = requests.get(url).json()
print(response)
print(type(response))

# 데이터 중 온도를 파싱하시오.
temp = response['main']['temp']
print(f'온도 = {temp}')

#%%
import requests
from pprint import pprint
# 서울의 위도 37.56 / 경도 126.97
city = 'Seoul,KR'
api_key = 'f3c91e30a2c9ad7700a90abfc782ac4b'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url).json()
print(response)
print(type(response))

# %%
