from flask import Blueprint, render_template, request, redirect
import pymysql as db

register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['GET'])
def register1():
    return render_template('/register.html')

@register_blueprint.route('/register', methods=['POST'])
def register2():
    uid = request.form['uid']
    name = request.form['name']
    hp = request.form['hp']
    pos = request.form['pos']
    dep = request.form['dep']

# 1단계 - 데이터베이스 접속
    conn = db.connect(host='192.168.10.114',
                  user='khr',
                  password='1234',
                  db='khr',
                  charset='utf8')

# 2단계
    cursor = conn.cursor()

# 3단계
    sql = "INSERT INTO `MEMBER` VALUES ('"+uid+"', '"+name+"', '"+hp+"', '"+pos+"', "+dep+", NOW());"
    cursor.execute(sql)

# 4단계
    conn.commit()

# 5단계
    conn.close()

    return redirect('/list')

