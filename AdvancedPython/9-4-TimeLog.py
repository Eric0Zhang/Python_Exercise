from random import randint
from functools import wraps  # functools的wraps可以保存原函数的元数据

import time
import logging

# 记录被装饰的函数执行的时间, 并设置超时时间, 记录超时情况


def warn(timeout):
    def decorator(func):
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout)
                logging.warning(msg)
            return res

        def setTimeout(k):
            # 关键字nonlocal知名timeout不是局部变量,
            # 系统将为被装饰函数创建一个闭包的timeout
            nonlocal timeout
            timeout = k
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator


@warn(1.5)
def test():
    print('In test')
    # 有概率连续几次都是1,那么就可能会超时,有一次0就退出了
    while randint(0, 1):
        time.sleep(0.5)


for _ in range(30):
    test()

test.setTimeout(1)
for _ in range(30):
    test()
