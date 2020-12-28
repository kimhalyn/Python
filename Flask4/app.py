"""
날짜 : 20/12/24
이름 : 김하린
내용 : 파이썬 Flask 웹 프로그래밍
"""

from flask import Flask, render_template, redirect
from Flask4.views.list import list_blueprint
from Flask4.views.register import register_blueprint

app = Flask(__name__)

# 블루프린트 모듈 등록
app.register_blueprint(list_blueprint)
app.register_blueprint(register_blueprint)

@app.route('/')
def index():
    return redirect('/register')

if __name__ == '__main__':
    app.run()