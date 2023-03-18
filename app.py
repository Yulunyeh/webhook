from flask import Flask 

app = Flask(__name__)

# domain root
@app.route("/", methods=["POST"])
def callback():
    return "Hello World!!"
