"""
날짜 : 2020/12/24
이름 : 김하린
내용 : 파이썬 데이터베이스 프로그래밍
"""

import pymysql as db

# 1단계 - 데이터베이스 접속
conn = db.connect(host='192.168.10.114',
                  user='khr',
                  password='1234',
                  db='khr',
                  charset='utf8')

# 2단계 - sql 실행 객체 생성
cursor = conn.cursor()

# 3단계 - sql 실행
sql = "UPDATE `USER1` SET `hp`='010-1234-2222' where `uid`='p101';"

cursor.execute(sql)

# 4단계 - sql 실행 확정
conn.commit()

# 5단계- 데이터베이스 종료
conn.close()

print('UPDATE 완료')