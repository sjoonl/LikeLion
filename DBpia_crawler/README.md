# 파일럿 프로젝트(데이터 분석 기본 실습)
## 주제: DBpia 데이터 크롤링


### 과제 개요
 * 국내 최대 논문 플랫폼인 디비피아(DBpia) 사이트내의 논문정보를 불러와 CSV파일로 저장하는 프로그램
 * 논문정보: 논문 제목, 저자, 학회, 날짜, 이용자 수, 요약


### 데이터 수집 전략
 * DBpia 내에서 논문 키워드를 입력하면 해당 키워드가 들어간 논문들의 정보를 수집한다.  [DBpia 사이트로 이동](https://www.dbpia.co.kr/)
 * 파이썬3를 통해 작성하였고 Beautifulsoup과 selenium을 이용하였다.
 * 크롬 드라이버 이용 [크롬 드라이버 다운로드](https://chromedriver.chromium.org/downloads)

### 설치
```python3
pip install selenium
pip install BeautifulSoup
```
 
### 실행
```python3
crawling_page_number = 클롤링할 페이지 수
sel_a.send_keys("검색어 입력")
path = "크롬드라이버 경로지정"
```
