from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello and Welcome to this demo!"

if __name__ == '__main__':
    app.run(debug=True)
