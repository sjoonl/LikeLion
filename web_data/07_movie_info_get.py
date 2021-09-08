from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://movie.naver.com/movie/running/current.naver'
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

print(soup.title)


movie_data_list = ['제목', '평점']



#제목 가져오기
# 1. 우선 제목 하나만 먼저 가져와 본다.
title_data_one = soup.find("dt",class_ = "tit").find("a").text
#print(title_data_one)

#2. 전체 데이터 가져오기
movie_title = []
title = soup.find_all('dt', class_ = 'tit')
for one in title:
    title_one = one.find("a").text
    movie_title.append(title_one)
print(movie_title)
print(len(movie_title))



#평점 점수 가져오기

score_list = []
score_all = soup.find_all('dl', class_  =  'info_star')
for one in score_all:
    one_score = one.find('span', class_ = 'num').text
    score_list.append(one_score)

print(len(score_list))

#예매율 정보 가져오기
# exp_list = []
# exp_all = soup.find_all('dl', class_  =  'info_exp')
# for one in exp_all:
#     exp = one.find('span', class_ = 'num').text
#     if exp is not None:
#         exp_list.append(exp)
#     else:
#         exp_list.append("0")
#         print("x")
# print(len(exp_list))

#예매율 정보 가져오기2

exp_list = []
exp_all = soup.find_all('dd', class_  =  'star')
for one in exp_all:
    if one.find('dl', class_ = 'info_exp') is not None:
        exp_list.append(one.find('dl', class_ = 'info_exp').text)
    else:
        exp_list.append("0")

print(len(exp_list))

#참여명수 가져오기

people_number_list = []
people_all = soup.find_all('dl', class_  =  'info_star')
for one in people_all:
    number = one.find('em').text
    people_number_list.append(number)




print(people_number_list)

#개요 가져오기


import pandas as pd
#파일 만들기
#movie_title  score_list people_number_list

dict_dat = {"영화제목":movie_title,
            "평점":score_list,
            "평점 참여명수":people_number_list,
            "예매 율":exp_list}

dat = pd.DataFrame(dict_dat)

print(dat)

dat.to_csv("naver_movie_info.csv", index = False)
dat.to_excel("naver_movie_info.xlsx", index = False)

#수정