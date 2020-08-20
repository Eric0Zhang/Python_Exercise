from inspect import signature

# 带参数的装饰器,根据传输的参数实现不同的装饰器
# *args传递的是参数列表,如传入1,2,3,则*args得到['a','b','c']
# **kargs传递的是参数字典,如传入a=1,b=2,c=3则**kargs得到{'a':1,'b':2,'c':3}
# 可以查看专题:包裹传递和解包


def typeassert(*ty_args, **ty_kargs):
    def decorator(func):
        # 获得func的参数列表 本例中即(a,b,c)
        sig = signature(func)
        # 将typeassert的类型列表与func参数列表绑定
        # 形成形如{(a,class"int"),(b,class"str"),(c,class"int")}的绑定字典,
        # key是func的参数列表, value是ty的类型列表
        # 这里可能有三个参数,但是typeassert只检查前两个,所以用partial绑定
        btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments
        # wrapper的参数列表就是func的传入参数列表

        def wrapper(*args, **kargs):
            # 迭代传入参数的类型:值字典
            # name是变量名 obj是传入的值
            for name, obj in sig.bind(*args, **kargs).arguments.items():
                # 传入参数函数变量名是否在检查的变量中
                if name in btypes:
                    # 如果类型不是ty规定的类型,则异常
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"%s" must be "%s"' %
                                        (name, btypes[name]))
            return func(*args, **kargs)
        return wrapper
    return decorator


@typeassert(int, str, list)
def f(a, b, c):
    print(a, b, c)


f(1, 'abc', [1, 2, 3])
f(1, 2, [1, 2, 3])
