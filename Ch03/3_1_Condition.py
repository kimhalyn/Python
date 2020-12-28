"""
날짜 : 2020/12/22
이름 : 김하린
내용 : 파이썬 조건문 실습하기 (switch문 없음)
"""

# if
num1, num2 = 1, 2
if num1 > 0:
    print('num1은 0보다 크다.')

if num1 < num2:
    print('num1은 num2보다 작다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 그리고 num2는 1보다 크다.')

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    """조건이 참일 때"""
    print('num3은 num4보다 크다.')
else:
    """조건이 거짓일 때"""
    print('num3은 num4보다 작다.')

# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2는 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

# 연습문제
score = 86

if score >= 90 and score <= 100:
    print('A 입니다.')
elif 80 <= score < 90:
    print('B 입니다.')
elif 70 <= score < 80:
    print('C 입니다.')
elif 60 <= score < 70:
    print('D 입니다.')
else:
    print('F 입니다.')