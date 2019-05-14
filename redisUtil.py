import redis


class RedisUtil():
    def __init__(self):
        pool = redis.ConnectionPool(host='140.143.161.107', port=6379, db=0, password="q1w2e3r4t5", encoding="utf-8",
                                    decode_responses=True)
        self.__pool = pool

    # 保存数据
    # expire：过期时间，单位秒
    def r_set(self, key, value, expire=None):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.set(key, value, ex=expire)

    # 获取数据
    def r_get(self, key):
        redi = redis.Redis(connection_pool=self.__pool)
        value = redi.get(key)
        if value is None:
            return None
        value = value.decode("UTF-8")
        return value

    # 删除数据
    def r_del(self, key):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.delete(key)

    def r_setList(self, key, values):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.lpush(key, values)

    def r_getList(self, key):
        redi = redis.Redis(connection_pool=self.__pool)
        _list = redi.lrange(key, 0, -1)
        return _list

    def bathSave(self, key, value):
        redi = redis.Redis(connection_pool=self.__pool)
        redi.sadd(key, value)
