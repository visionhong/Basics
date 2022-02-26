# 템플릿 상속
# {% extends "<부모 템플릿의 이름>" %},
# {% block %} <대체할 코드>{% endblock%}

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def temp_test():
    return render_template("09_2.html", my_string="템플릿 테스트", my_list=[111, 222, 333, 444, 555, 666, 777])

if __name__ =="__main__":
    app.run(debug=True)