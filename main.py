from bs4 import BeautifulSoup
import requests
import re


html_site = requests.get('https://www.imdb.com/calendar/').text #the site were getting the info from

soup = BeautifulSoup(html_site, 'lxml')

movies = soup.find_all('div', id =re.compile('^main'))

for movie in movies:
    movie_name = movies.a.text
    release_date = movies.h4.text
    movie_info = movies.a['href']
    print(f'Movie Name: {movie_name}')
    print(f'Release Date: {release_date}')
    print(f'Movie Info: https://www.imdb.com/{movie_info}')


