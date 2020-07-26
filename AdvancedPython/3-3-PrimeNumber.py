class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2,k):
            if k%i == 0:
                return False
        return True
    
    # 把iter方法实现为生成器函数
    def __iter__(self):
        for k in range(self.start, self.end+1):
            if self.isPrimeNum(k):
                yield k # 每次遇到素数, 执行一次迭代, 返回该素数

# for循环的逻辑: 调用对象的iter, 即迭代器对象, 
# 然后反复调用迭代器对象的next方法, 
# 每次next对于生成器函数, 将一直执行到下一次yield位置
for x in PrimeNumbers(1,100):
    print(x) 
