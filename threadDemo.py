#!/usr/bin/python3
import _thread
import time
import requests

url = "http://localhost:8080/api/segment/get/biz-order-segment"
# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 1000:
        response = requests.get(url)
        # time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, response.text))
def startThread():
    try:
        _thread.start_new_thread(print_time, ("Thread-0", 1))
        _thread.start_new_thread(print_time, ("Thread-1", 1))
        _thread.start_new_thread(print_time, ("Thread-2", 1))
        _thread.start_new_thread(print_time, ("Thread-3", 1))
    except:
        print("Error: 无法启动线程")
    while 1:
        pass

if __name__ == '__main__':
    startThread()
