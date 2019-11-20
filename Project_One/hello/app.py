from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'

@app.route('/hi')
@app.route('/hello')
@app.route('/ciao')          #可以叠加的绑定
def say_hello():
    return '<h1>hello flask!</h1>'

# route with var 
@app.route('/greet/<name>')  #第二个/后面的<name>相当于动态request URL变量
def greet(name):
    return '<h1>hello, %s!</h1>' % name
# example.com/greet/bar 会触发这个动态

#可以给上个例子添加默认值
@app.route('/greet', defaults={'name':'Programmer'})   #default 用一个字典形式 
@app.route('/greet/<name>')
def greet_(name):  #亦可再次设定默认值 name='Programmer'
    return '<h1>hello, %s!</h1>' % name

#want to test more about git