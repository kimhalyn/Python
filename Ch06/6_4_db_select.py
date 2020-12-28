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

# 2단계 - 실행 객체 새성
cursor = conn.cursor()

# 3단계 - sql 실행
sql = "SELECT * FROM `USER1`;"
cursor.execute(sql)

# 4단계 - 결과출력
for row in cursor.fetchall():
    print('------------------------')
    print('아이디 : ', row[0])
    print('이름 : ', row[1])
    print('휴대폰 : ', row[2])
    print('나이 : ', row[3])
    print('------------------------')

# 5단계 - 데이터베이스 종료
conn.close()