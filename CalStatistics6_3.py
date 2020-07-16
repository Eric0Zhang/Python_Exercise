def getNum(): #获取用户的输入数据
    nums = []
    count = 0
    while True:
        count+=1
        print('请输入第%d个数据（回车结束）:' % count,end='')
        iNum = input()
        if iNum == '':
            break
        else:
            intNum = eval(iNum)
            nums.append(intNum)
            print(nums)
    return nums

def mean(numbers):#平均值
    s = 0.0
    for num in numbers:
        s+=num
    s/=len(numbers)
    return s

def dev(numbers, mean): #计算方差
    sdev = 0.0
    for num in numbers:
        sdev+=(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):#中位数
    sorted(numbers)
    size = len(numbers)
    if size%2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

def main():
    n = getNum()
    m = mean(n)
    print("平均数：{}，方差：{:.2}，中位数：{}".format(m,dev(n,m),median(n)))

main()