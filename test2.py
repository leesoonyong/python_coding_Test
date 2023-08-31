import requests
from bs4 import BeautifulSoup

# 크롤링할 페이지 URL
url = 'https://news.naver.com/main/home.naver'

# HTTP GET 요청
response = requests.get(url)

# 응답코드가 200이 아닌 경우 예외처리
if response.status_code != 200:
    raise Exception('Failed to retrieve news articles.')

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 기사 제목과 링크 추출
news_articles = soup.select('.hdline_article_tit > a')

# 결과 출력
for article in news_articles:
    title = article.text.strip()
    link = article['href']
    print(f'Title: {title}')
    print(f'Link: {link}')
    print('---')