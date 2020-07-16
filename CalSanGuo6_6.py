import jieba
def getText():
    txt = open("threekingdoms.txt","r",encoding='utf-8').read()
    words = jieba.lcut(txt)
    return words

words = getText()
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word in ["诸葛亮","孔明曰","孔明"]:
        rword = "孔明"
    elif word in ["关公","云长","关羽"]:
        rword = "关羽"
    elif word in ["玄德","玄德曰","刘备"]:
        rword = "刘备"
    elif word in ["孟德","曹操"]:
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
excludes = {"将军","却说","二人","荆州","不可","不能","如此","商议","如何","主公","军士","左右","军马","引兵","次日","大喜","天下","东吴","于是","今日","不敢","魏兵","陛下","一人","都督","人马","不知","汉中","只见","众将","后主","丞相"}
for word in excludes:
    del counts[word]
items = list(counts.items())#键值对转换为元组，成为列表的元素
items.sort(key=lambda x:x[1],reverse=True)#针对元素的第二项，也就是字典的值，单词数量进行从大到小排序

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))#左对齐10个字符 右对齐5个字符