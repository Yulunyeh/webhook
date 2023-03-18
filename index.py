from flask import Flask 

app = Flask(__name__)

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
