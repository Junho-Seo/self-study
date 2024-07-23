## 2987. 복잡한 자료구조 lv3
# G
#%%
data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]

#  first_data 변수에 비어있는 dict를 할당한다.
first_data = {}

# '제목'key에 문제의 제목에 해당하는 값을 찾아 할당한다.
first_data['제목'] = data[0]['results'][0]['properties']['제목']['title'][0]['plain_text']

'''
코드 설명
data[0]: data 리스트의 첫 번째 딕셔너리를 가져옴.
['results'][0]: results 키의 첫 번째 리스트 항목을 가져옴.
['properties']['제목']['title'][0]: 제목의 title 리스트에서 첫 번째 항목을 가져옴.
['plain_text']: 첫 번째 항목의 plain_text 값을 가져옴.

요약
[0]은 리스트에서 첫 번째 요소를 선택하는데 사용됩니다.
데이터 구조가 리스트 형태일 때, 원하는 요소를 가져오기 위해 인덱싱을 사용합니다.
인덱스 0은 첫 번째 요소를 의미합니다.

'''

# '일차'key에는 일차에 해당하는 값을 '정수'로 할당한다.
first_data['일차'] = int(data[0]['results'][0]['properties']['일차']['number'])

# '단계'key에는 단계에 해당하는 값을 찾아 '{value}단계'가 되도록 값을 변경하여 할당한다.
first_data['단계'] = f"{data[0]['results'][0]['properties']['단계']['select']['name']}단계"

# '과목'key에는 과목에 해당하는 값을 찾아 할당한다.
first_data['과목'] = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']

print(first_data)

#%%
data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]

# first_data 변수에 비어있는 dict를 할당한다.
# '제목'key에 문제의 제목에 해당하는 값을 찾아 할당한다.
# '일차'key에는 일차에 해당하는 값을 '정수'로 할당한다.
# '단계'key에는 단계에 해당하는 값을 찾아 '{value}단계'가 되도록 값을 변경하여 할당한다.
# '과목'key에는 과목에 해당하는 값을 찾아 할당한다.
first_data = {}

first_data['제목'] = data['제목']
print(first_data)