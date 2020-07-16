for num in range(2,100):
    flag=0
    for div in range(2,num):
        if num%div==0:
            flag+=1
    if flag==0:
        print(num)
    