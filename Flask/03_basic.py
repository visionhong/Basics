from flask import Flask

app = Flask(__name__)

@app.route('/username/<userName>')  # <userName> 이게 함수의 인자값 즉 변수 (동적으로 변경되는 부분)
def get_uriName(userName):
    return 'userName:' + userName


if __name__ == '__main__':
    app.run()