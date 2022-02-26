from flask import Flask

app = Flask(__name__)  # app이라는 flask 객체 생성

# @ : 데코레이터
@app.route('/')  # root url로 사용자가 접속을 하게 되면 아래 뷰함수를 호출한다.
def hello():
    return "Hello World!!"


# logic: user -> router -> 뷰함수 -> 템플릿(html 등) -> user

'''
라우팅: 복잡한 URI를 쉽게 처리하도록 하는 기능
Flask에서는 route() 데코레이터(@) 사용한다.
'''

if __name__ == "__main__":
    app.run()