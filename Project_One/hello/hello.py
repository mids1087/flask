from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Greet, %s!</h1>' % __name__

# test commit from .py