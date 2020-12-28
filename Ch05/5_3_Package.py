"""
날짜 : 2020/12/23
이름 : 김하린
내용 : 파이썬 패키지 실습하기
"""

from Ch05.sub3.Account import Account
from Ch05.sub3.calc import *            # 패키지에 있는 모든 파일 임포트 가능

nh = Account('농협은행', '111-23-4567', '김파이', 10000 )
nh.deposit(20000)
nh.withdraw(5000)
nh.show()

r1 = plus(1, 2)
r2 = minus(1, 2)
r3 = multi(1, 2)
r4 = div(1, 2)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)