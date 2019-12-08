import redis

class Cache():

    def __init__(self):
        self.cache = redis.Redis(
            host='127.0.0.1',
            port=6379,
            decode_responses= True
        )

    def set_key(self, key, value, expire):
        return self.cache.set(key, value, ex=expire)

    def exists(self, key):
        return self.cache.exists(key)

    def get_keys(self):
        return self.cache.keys(pattern='*')

    def get_key(self, key):
        return self.cache.get(key)

    def append_key(self, key, value):
        return self.cache.append(key, value)

    def delete_key(self, key):
        return self.cache.delete(key)

    def increment(self, key, amount):
        return self.cache.incr(key, amount)

    def decrement(self, key, amount):
        return self.cache.decr(key, amount)


if __name__ == "__main__":
    c = Cache()
    set_key = c.set_key('foo', 'bar', None)
    set_key = c.set_key('foo1', 'bar', 10)
    keys = c.get_keys()
    key = c.get_key('foo')
    increment = c.increment('one', 1)
    exists = c.exists('one')
    decrement = c.decrement('one', 1)
    keys = c.get_keys()
