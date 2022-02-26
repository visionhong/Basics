# jinja 에서 템플릿 표현식

# {% :block_start_string     %} : block_end_string (템플릿에서의 프로그래밍 영역(제어, 반복문 등)을 넣기 위한 기호)
# {{ :variable_start_string  }} : variable_end_string  변수를 출력하기 위해 사용(모든 형식의 변수 가능 /문자열/리스트 등등)
# {# :comment_start_string   #} : comment_start_string  주석을 넣기위해 사용

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def temp_test():
    return render_template('08.html', my_string="템플릿 테스트", my_list=[11, 22, 33, 44, 55, 66, 77])



if __name__ =="__main__":
    app.run(debug=True, port=8000)

