import requests
import threading
import redisUtil

re = redisUtil.RedisUtil()


def thread_write_proxy(proxy):
    re.bathSave("usableIp", proxy)


def thread_test_proxy(proxy):
    url = "http://www.baidu.com/"
    header = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }
    try:
        response = requests.get(
            url, headers=header, proxies={"http://": proxy}, timeout=1000)
        print(response.status_code)
        if response.status_code == 200:
            print("该代理IP可用：", proxy)
            # normal_proxies.append(proxy)
            thread_write_proxy(proxy)
        else:
            print("该代理IP不可用：", proxy)
    except Exception:
        print("该代理IP无效：", proxy)
        pass


# 验证已得到IP的可用性
def test_proxies(proxies):
    proxies = proxies
    _str = "".join(proxies)
    strlist = _str.split(',')
    print(strlist)
    for i in range(len(strlist)):
        print(strlist[i])
    # print("test_proxies函数开始运行。。。\n", proxies)
    for i in range(len(strlist)):
        test = threading.Thread(target=thread_test_proxy, args=(strlist[i],))
        test.start()
    # for proxy in proxies:
    #     test = threading.Thread(target=thread_test_proxy, args=(proxy,))
    #     test.start()


if __name__ == '__main__':
    proxies = re.r_getList("proxy_ip")
    test_proxies(proxies)
