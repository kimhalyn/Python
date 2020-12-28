"""
날짜 : 2020/12/23
이름 : 김하린
내용 : 파이썬 내장함수 실습하기
"""

import time
import calendar as cal
import math, random

# all() : 리스트에서 0이 포함되었는지 확인
list1 = [1, 2, 3, 4, 5]
list2 = [0, 2, 3, 4, 5]

r1 = all(list1)
r2 = all(list2)

print('r1 : ', r1)
print('r2 : ', r2)

# any() : 리스트에서 True 값이 1개라도 있으면 전체 True, 모두 False면 전체 False
list3 = [0, 1, 2]
list4 = [0, '', None] # empty String , null=None

r3 = any(list3)
r4 = any(list4)

print('r3 : ', r3)
print('r4 : ', r4)

# enumerate() : for문에서 리스트의 인덱스와 값을 리턴하는 함수
list5 = ['이순신', '김유신', '장보고']

for i, name in enumerate(list5):
    print(i, name)

# lambda : 람다식을 정의하는 함수
def sum1(a, b):
    return a+b

sum2 = lambda a, b: a+b

rs1 = sum1(2, 3)
rs2 = sum2(2, 3)

print('rs1 : ', rs1)
print('rs2 : ', rs2)

# time() : 날짜, 시간 구하는 함수, 임포트로 time 모듈을 추가해줘야 함
t1 = time.time()
print('t1 : ', t1)

t2 = time.ctime()
print('t2 : ', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)

hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일' % (year, month, date))
print('%s시 %s분 %s초' % (hour, min, sec))

# calendar() : 달력 구하는 함수, 모듈 추가해야 함
c1 = cal.calendar(2020)
print('c1 : ', c1)

# abs() : 절대값
res1 = abs(-5)
print('res1 : ', res1)

# ceil() : 무조건 올림
res2 = math.ceil(1.2)
res3 = math.ceil(1.8)

print('res2 : ', res2)
print('res3 : ', res3)

# floor() : 무조건 내림
res4 = math.floor(1.2)
res5 = math.floor(1.8)

print('res4 : ', res4)
print('res5 : ', res5)

# round() : 반올림
res6 = round(1.2)
res7 = round(1.8)

print('res6 : ', res6)
print('res7 : ', res7)

# random() : 모듈추가
num1 = random.random() # 0 ~ 1 사이의 실수
print('num1 : ', num1)

num2 = num1 * 10    # 1 ~ 10 사이 실수
print('num2 : ', num2)

num3 = math.ceil(num2) #1 ~ 10 사이 정수
print('num3 : ', num3)

num4 = math.ceil(random.random()*10)
print('num4 : ', num4) #1 ~ 10 사이 정수