from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!\nI am Indrajith</p>"

app.run(debug=True) 