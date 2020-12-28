"""
날짜 : 2020/12/24
이름 : 김하린
내용 : 파이썬 Flask 블루프린트 실습하기

blueprint
- 파이썬 Flask 웹프로그래밍에서 Template(HTML) 컴포넌트 개발을 위한 객체
- 하나의 Template(HTML)은 하나의 컴포넌트를 가짐
"""

from flask import Flask, render_template
from Flask3.views.index import index_blueprint
from Flask3.views.sub1.sub1_1 import sub1_1_blueprint
from Flask3.views.sub1.sub1_2 import sub1_2_blueprint
from Flask3.views.sub2.sub2_1 import sub2_1_blueprint
from Flask3.views.sub2.sub2_2 import sub2_2_blueprint


app = Flask('__name__')

# 블루프린트 모듈(템플릿 컴포넌트) 등록
app.register_blueprint(index_blueprint)
app.register_blueprint(sub1_1_blueprint)
app.register_blueprint(sub1_2_blueprint)
app.register_blueprint(sub2_1_blueprint)
app.register_blueprint(sub2_2_blueprint)

if __name__ == '__main__':
    app.run()