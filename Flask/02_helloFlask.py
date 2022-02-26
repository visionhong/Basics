from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
# 맨 끝에 / 가 있으면 url에서 /를 붙여도, 안붙여도 결과를 얻을 수 있음
# 만약 뒤에 /를 붙이지 않으면 url에서도 /를 붙이지 않을때만 결과가 나옴.

def hello_flask():
    return "welcome to flask"

if __name__ == "__main__":
    app.run()