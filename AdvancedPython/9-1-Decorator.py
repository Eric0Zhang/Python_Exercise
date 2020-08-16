# 除了直接在代码中加入缓存程序的修饰外,
# 还可以用外包一层wrap函数的方式实现
def memo(func):
    cache = {}
    # 传输参数使用* 表示函数的参数列表,每个元素用逗号分隔
    def wrap(*args):
        # 这里args是一个元组,包含所有参数, 
        # cache的key就是args构成的元组
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

# 斐波那契数列 可以用缓存的形式,用空间换时间,
# 不然像下面这样直接递归会有大量的重复计算
@memo
def fibonacci(n, cache = None):
    # if cache is None:
    #     cache = {}
    # if n in cache:
    #     return cache[n]
    if n<=1:
        return 1
    # cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return fibonacci(n-1) + fibonacci(n-2)

#fibonacci = memo(fibonacci)
print(fibonacci(100))

# 一共有n个台阶的楼梯,从下面走到上面,一次只能迈steps步,
# 并且不能后退,走完共有多少种方法
@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n>0:
        for step in steps:
            count += climb(n-step, steps)
    return count

print(climb(100,(1,2,3)))

