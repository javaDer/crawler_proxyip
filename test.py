import redisUtil
import requests
pr = redisUtil.RedisUtil()
from faker import Factory

# zh_CN 表示中国大陆版
fake = Factory().create('zh_CN')
# 产生随机手机号
print(fake.phone_number())
# 产生随机姓名
print(fake.name())
# 产生随机地址
print(fake.address())
# 随机产生国家名
print(fake.country())
# 随机产生国家代码
print(fake.country_code())
# 随机产生城市名
print(fake.city_name())
# 随机产生城市
print(fake.city())
# 随机产生省份
print(fake.province())
# 产生随机email
print(fake.email())
# 产生随机IPV4地址
print(fake.ipv4())
# 产生长度在最大值与最小值之间的随机字符串
print(fake.pystr(min_chars=0, max_chars=8))

# 随机产生车牌号
print(fake.license_plate())
print(fake.ssn())
print(fake.text())
# 随机产生颜色
print(fake.rgb_color())  # rgb
print(fake.safe_hex_color())  # 16进制
print(fake.color_name())  # 颜色名字
print(fake.hex_color()) # 16进制

# 随机产生公司名
print(fake.company())


# 随机产生工作岗位
print(fake.job())
# 随机生成密码
print(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
# 随机生成uuid
print(fake.uuid4())
# 随机生成sha1
print(fake.sha1(raw_output=False))
# 随机生成md5
print(fake.md5(raw_output=False))

# 随机生成女性名字
print(fake.name_female())
# 男性名字
print(fake.name_male())
# 随机生成名字
print(fake.name())

# 生成基本信息
print(fake.profile(fields=None, sex=None))
print(fake.simple_profile(sex=None))
url = "http://localhost:8080/api/segment/get/biz-order-segment"
response = requests.get(url)
print(response.text)
# 随机生成浏览器头user_agent
print(fake.user_agent())

# for i in range(10):
#    pr.bathSave("test",i)
#    print(i+1)