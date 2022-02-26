from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('05.html')  # templates 폴더에서 해당 html을 찾음 (virtual environment 필요 )

if __name__ == "__main__":
    app.run()