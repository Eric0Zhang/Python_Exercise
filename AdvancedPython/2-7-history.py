from random import randint
from collections import deque
import pickle

q = deque([], 5)

# history_file = open('history.his','w+')
# q = pickle.load(history_file)
n = randint(0,100)

def guess(k):
    if k==n:
        print('right')
        return True
    if k<n:
        print('%s is less than n' % k)
    else:
        print('%s is greater than n' % k)
    return False

while True:
    line = input('please input a number: ')
    if line.isdigit():
        k = int(line)
        q.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        print('recent five number guessed:')
        print(list(q))

#pickle可以存储一个对象到文件中取,再用Load取出
pickle.dump(q,open('history.his','w'))