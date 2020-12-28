"""
날짜 : 2020/12/21
이름 : 김하린
내용 : 파이썬 자료구조 딕셔너리 실습하기 {}
"""

# 딕셔너리(파이썬의 json_데이터를 객체화 시키는 문법)
dic1 = {1: 'C++', 2: 'java', 3: 'python'}
dic2 = {
        'kor': '대한민국',
        'usa': '미국',
        'jap': '일본',
        'chi': '중국'
}

dic3 = {
        101: [1, 2, 3],
        102: ['김춘추', '이순신', '강감찬'],
        103: [True, False, True]
}
# 딕셔너리 출력
print('dic1 : ', dic1)
print('dic2 : ', dic2)
print('dic3 : ', dic3)

print('dic1[1] : ', dic1[1])
print("dic2['kor'] : ", dic2['kor']) # 작은 따옴표 안에 또 작은따옴표 불가 -> 큰 따옴표 안에 작은 따옴표로 수정
print('dic3[102] : ', dic3[102])
print('dic3[102][1] : ', dic3[102][1])

# 딕셔너리 추가
dic1[4] = 'Javascript' 
print('dic1 : ', dic1)

dic2['aus'] = '호주'
print('dic2 : ', dic2)

dic3[104] = (7, True, 'Hello') # 튜플 추가
print('dic3 : ', dic3)


# 딕셔너리 제거
del dic1[1]
print('dic1 : ', dic1)

