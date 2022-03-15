import requests
import time

from tkinter import *

url_counter = "http://127.0.0.1:5000/?type=counter"
url_reset = "http://127.0.0.1:5000/?type=reset"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate,",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def tickets():
    entry1.delete(0, END)
    resp = requests.get(url = url_reset, headers = header, timeout = 1)
    start_time = time.time()
    for i in range(100000):
        resp = requests.get(url = url_counter, headers = header, timeout = 1)
        end_time = time.time()
        cha = end_time - start_time
        if cha >= 10:
            print('抢购时间:', cha)
            entry1.insert(3, '抢购结束，退出该程序。')
            break

# 画一个界面
MyWindow = Tk()
MyWindow.title('月饼抢购程序')

Label(MyWindow, text='运行结果 ').grid(row=0, column=0, padx=10, pady=10, ipady=10, sticky='w')

entry1 = Entry(MyWindow)
entry1.grid(row=0, column=1, padx=10, pady=10, ipady=10, sticky='w')

Button(MyWindow, text='退出', command=MyWindow.quit).grid(row=1, column=0, sticky=W, padx=10, pady=10)
Button(MyWindow, text='运行', command=tickets).grid(row=1, column=1, sticky=W, padx=10, pady=10)

MyWindow.mainloop()







