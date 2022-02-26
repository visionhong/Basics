from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World!!</h1>"

# 타입의 username 파라미터(default 값은 String)
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"

# int 타입의 post_id 파라미터 이용
@app.route('/post/<int:post_id>')  # 무조건 int형만 와야함. (string, float 에러)
def show_post(post_id):
    return f"Post: {post_id}"

# float 타입의 pi 파라미터
@app.route('/circle/<float:pi>')  # 무조건 float형만 받음
def show_pi(pi):
    return f'Pi: {pi}'


if __name__ == '__main__':
    app.run()