def getText():#把文本归一化，全部编程小写单词
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())#键值对转换为元组，成为列表的元素
items.sort(key=lambda x:x[1],reverse=True)#针对元素的第二项，也就是字典的值，单词数量进行从大到小排序

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))#左对齐10个字符 右对齐5个字符