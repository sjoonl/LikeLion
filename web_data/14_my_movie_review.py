from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://movie.naver.com/movie/point/af/list.naver?&page='

comments = []
for i in range(1,51,1):
    new_url = url + str(i)
    page = urlopen(new_url)
    soup = BeautifulSoup(page,'html.parser')

    comment_all = soup.find_all('td', class_='title')
    print(len(comment_all))
    for one in comment_all:
        temp = list(one.children)[6].strip()
        comments.append(temp)
print(len(comments))


import pandas as pd

dict_dat = {"영화 댓글":comments}
dat = pd.DataFrame(dict_dat)
dat.to_csv("나의 영화댓글.csv", index = False)
dat.to_excel("나의 영화댓글.xlsx", index = False)


f = open("나의 영화댓글.csv", encoding='utf-8')
text = f.read()
print(text)

from wordcloud import WordCloud

from matplotlib import rc

rc('font', family="NanumGothic")

wcloud = WordCloud('D2Coding.ttf', max_words = 1000, relative_scaling = 0.2).generate(text)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()