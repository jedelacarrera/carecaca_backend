import time


class MemoizationClient:
    def __init__(self):
        self.data = {}

    def get(self, key):
        value = self.data.get(key)
        if value is not None and time.time() < value[1]:
            return value[0]

        return None

    def put(self, key, response, ttl):
        final_time = time.time() + ttl
        self.data[key] = (response, final_time)


client = MemoizationClient()


def cache_decorator(name, ttl, index=0):
    def decorate(f):
        def execute_function(*args, **kwargs):
            arg = args[index]
            value = client.get((name, arg))
            if not value:
                value = f(*args, **kwargs)
                client.put((name, arg), value, ttl)
            return value

        return execute_function

    return decorate
