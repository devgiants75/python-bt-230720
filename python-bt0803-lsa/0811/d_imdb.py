### 인터넷 영화 데이터베스에서 영화 정보 수집 ###

# IMDb: Internet Movie Database

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.imdb.com/?ref_=nv_home'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def fetch_movie_data(start):
    url = BASE_URL.format(start)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    movie_containers = soup.select('.ipc-poster-card ipc-poster-card--baseAlt ipc-poster-card--dynamic-width topten-title ipc-sub-grid-item ipc-sub-grid-item--span-2')
    for movie in movie_containers:
        image = movie.div.a
        title = movie.a.span
        print(f'{image} {title}')

fetch_movie_data(0)