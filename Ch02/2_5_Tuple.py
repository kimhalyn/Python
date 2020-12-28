"""
날짜 : 2020/12/21
이름 : 김하린
내용 : 파이썬 자료구조 튜플 실습하기 _ 튜플도 list와 동일하나 원소 값을 변경할 수 없음 ()
"""

# 튜플
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3
tuple3 = ('사과', '오렌지', '바나나', '포도')

list1 = [1, 2, 3]

# 튜플 원소 출력
print('tuple1[0] : ', tuple1[0])
print('tuple2[2] : ', tuple2[2])
print('tuple3[3] : ', tuple3[3])

# 타입 확인
list1 = [1, 2, 3]

print('tuple1 type : ', type(tuple1))
print('list1 type : ', type(list1))

# 리스트와 튜플 차이점
tuple1[0] = 5 # 에러남.
