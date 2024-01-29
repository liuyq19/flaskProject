from flask import Flask,render_template

app = Flask(__name__)


class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

@app.route('/')
def index():
    hobby = "游戏"
    person = {
        "name": "张三",
        "age": 181
    }
    user = User("李四", "xx@qq.com")
    return render_template("index.html", hobby=hobby, person=person, user=user)


if __name__ == '__main__':
    app.run(debug=True)