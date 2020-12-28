from flask import Blueprint, render_template
import pymysql as db

list_blueprint = Blueprint('list', __name__)

@list_blueprint.route('/list')
def list():


    # 1단계 - 데이터베이스 접속
    conn = db.connect(host='192.168.10.114',
                      user='khr',
                      password='1234',
                      db='khr',
                      charset='utf8')

    # 2단계
    cursor = conn.cursor()

    # 3단계
    sql = "SELECT * FROM `MEMBER`;"
    cursor.execute(sql)

    # 4단계
    members = []

    for row in cursor.fetchall():
        member = {
            'uid': row[0],
            'name': row[1],
            'hp': row[2],
            'pos': row[3],
            'dep': row[4],
            'rdate': row[5]
        }

        members.append(member)

    # 5단계

    conn.close()


    return render_template('/list.html', members=members)