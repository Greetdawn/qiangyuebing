from flask import Flask
from flask import render_template, request, jsonify
from flask import session
import os

app = Flask(__name__)
app.secret_key = 'greetdawn'

count = 0
@app.before_request
def before():
    valu = request.args.get('type')
    if valu == 'counter':
        counter()
    elif valu == 'reset':
        global count
        count = 0
        f = open('counter.txt', 'w')
        f.write(str(count))
        f.close()


@app.route('/')  # 主页地址,“装饰器”
def news():
    f = open('counter.txt','r')
    count = f.read()
    # print(count)
    title = '月饼抢购'
    the_tastes = {
        '1': ['豆沙味', '178'],
        '2': ['西瓜味', '223'],
        '3': ['哈密瓜味', '13'],
        '4': ['杏仁味', '48'],
    }

    context = {
        'title': title,
        'the_tastes': the_tastes,
        "counter": count,
    }
    f.close()
    return render_template('index.html', context=context)

# 构造计数器
def counter():
    global count
    count += 1
    f = open('counter.txt', 'w')
    f.write(str(count))
    f.close()


if __name__ == '__main__':
    app.run(host='192.168.1.81', threaded=True, port=80)