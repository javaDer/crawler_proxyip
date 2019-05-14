import requests
import re
import random
import redisUtil
from bs4 import BeautifulSoup

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    "Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 45.0.2454.101Safari / 537.36"
]
pr = redisUtil.RedisUtil()


def ip_parse_xici(page):
    """
    :param page: 采集的页数
    :return:
    """
    ip_list = []
    for pg in range(1, int(page)):
        url = 'http://www.xicidaili.com/nn/' + str(pg)
        user_agent = random.choice(ua_list)
        my_headers = {
            'Accept': 'text/html, application/xhtml+xml, application/xml;',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Referer': 'http: // www.xicidaili.com/nn',
            'User-Agent': user_agent
        }
        try:
            r = requests.get(url, headers=my_headers)
            soup = BeautifulSoup(r.text, 'html.parser')
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
        else:
            data = soup.find_all('td')
            # 定义IP和端口Pattern规则
            ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')  # 匹配IP
            port_compile = re.compile(r'<td>(\d+)</td>')  # 匹配端口
            ips = re.findall(ip_compile, str(data))  # 获取所有IP

            ports = re.findall(port_compile, str(data))  # 获取所有端口
            check_api = "http://ip.taobao.com/service/getIpInfo2.php?ip="

            for i in range(len(ips)):
                if i < len(ips):
                    ip = ips[i]
                    api = check_api + ip
                    api_headers = {
                        'User-Agent': user_agent
                    }
                    try:
                        response = requests.get(url=api, headers=api_headers, timeout=2)
                        print("ip：%s 可用" % ip)
                    except Exception as e:
                        print("此ip %s 已失效：%s" % (ip, e))
                        del ips[i]
                        del ports[i]
            ips_usable = ips
            ip_list += [':'.join(n) for n in zip(ips_usable, ports)]  # 列表生成式
            print('第{}页ip采集完成'.format(pg))
    print(ip_list)
    return ip_list


if __name__ == '__main__':
    xici_pg = input("请输入需要采集的页数：")
    ip_list = ip_parse_xici(page=xici_pg)
    pr.r_setList("proxy_ip", ",".join(ip_list))
