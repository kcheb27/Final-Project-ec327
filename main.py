from flask import Flask
app = Flask(__name__)





print("hello")

@app.route('/upload',methods=["GET", "POST"])
def hello():
    return '<h1>Hello, cheese!</h1>'
