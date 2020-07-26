# 列表字符串等都是调用内部的迭代器来完成循环迭代
# 列表对象或者字符串对象都有__iter__方法返回迭代对象
# iter对象的next方法可以一次迭代每一项, 直到最后的StopIteration异常
# conections模块中有Iterator迭代器和Iterable可迭代对象,3.3以后移到了抽象类中即collections.abc中
from collections.abc import Iterator, Iterable
import requests

class WeatherIterator(Iterator):#继承Iterator
    def __init__(self, cities):#构造器
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s ' % (city, data['low'], data['high'])
    def __next__(self):#重构基类的虚函数__next__
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

#可迭代对象继承Iterable
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):#重构基类虚函数__iter__
        return WeatherIterator(self.cities)

weahter = WeatherIterable([u'北京',u'南京',u'天长'])
for x in weahter:
    print(x)