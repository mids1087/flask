from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Greet, %s!</h1>' % __name__

# test commit from .py 必须要在.git 主目录下commit 不然就在commit 后面添加 -a 所有
# try if commit -a works without add
