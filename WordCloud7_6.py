import jieba as jb
import wordcloud as wc
from imageio import imread

mask = imread("bj.png")

with open("sdxl.txt",'rt', encoding = "utf-8") as file:
    f = file.read()
    ls = jb.lcut(f)
    strfile = ''
    strfile = ' '.join(ls)
    w = wc.WordCloud(font_path='msyh.ttc', mask = mask, \
        width = 1000, height = 700, background_color = 'white')
    w.generate(strfile)
    w.to_file("sdxl.png")