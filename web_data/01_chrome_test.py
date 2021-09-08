from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
KOSPI = soup.find("span", id="KOSPI_now")

KOSDAQ = soup.find("span", id="KOSDAQ_now")

KOSPI_200 = soup.find("span", id="KPI200_now")

popular = soup.find("ul", id="popularItemList")

#select로 가져오는 방식
top10_name = soup.select("#popularItemList > li > a")
top10_price = soup.select("#popularItemList > li > span")

#find all 로 가져오는 방식
data = soup.find()


for i in top10_name:
    print(i.text)

for i in top10_price:
    print(i.text)


print("코스피 현재 지수는: ", KOSPI.text)
print("코스닥 현재 지수는: ", KOSDAQ.text)
print("코스피200 지수는: ", KOSPI_200.text)

print("인기 검색 종목", popular)

#수정