# 分词、词频、词云函数
import jieba
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# 默认停用词表，可自定义路径
STOPWORDS = set()
STOPWORDS_PATH = os.path.join(os.path.dirname(__file__), 'stopwords.txt')
if os.path.exists(STOPWORDS_PATH):
    with open(STOPWORDS_PATH, encoding='utf-8') as f:
        for line in f:
            STOPWORDS.add(line.strip())
else:
    # 常用停用词
    STOPWORDS = set(['的', '了', '和', '是', '在', '就', '都', '而', '及', '与', '着', '或', '一个', '没有', '我们', '你们', '他们', '我', '你', '他', '她', '它', '啊', '吧', '吗', '呢', '呀', '哦', '也', '还', '很', '但', '并', '被', '让', '给', '对', '与', '等', '这', '那', '其', '并', '已', '已', '去', '来', '会', '要', '说', '看', '让', '做', '用', '到', '为', '把', '从', '以', '等', '等'])

def segment_titles(titles, stopwords=STOPWORDS, min_len=2):
    """
    对标题列表进行分词，返回所有词的列表
    titles: pd.Series 或 list
    stopwords: 停用词集合
    min_len: 最小保留词长
    """
    words = []
    for title in titles:
        segs = jieba.lcut(str(title))
        words += [w for w in segs if w not in stopwords and len(w) >= min_len]
    return words

def get_top_words(words, top_n=30):
    """
    统计高频词
    words: 分词后词列表
    top_n: 返回前N高频
    """
    return Counter(words).most_common(top_n)

def plot_wordcloud(words, font_path=None, width=800, height=400, background_color='white', max_words=200):
    """
    绘制词云
    words: 分词后词列表
    font_path: 字体路径（如中文需指定）
    """
    text = ' '.join(words)
    wc = WordCloud(font_path=font_path, width=width, height=height, background_color=background_color, max_words=max_words)
    wc.generate(text)
    plt.figure(figsize=(width/100, height/100))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()