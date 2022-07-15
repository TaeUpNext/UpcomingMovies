from bs4 import BeautifulSoup
import requests
import re


html_site = requests.get('https://www.imdb.com/calendar/').text #the site were getting the info from

soup = BeautifulSoup(html_site, 'lxml')



#movies = soup.find_all('div', id=re.compile('^main'))
moviesDiv = soup.find('div', id = 'main')
moviesUL = moviesDiv.find_all('ul')

moviesReleaseDate = moviesDiv.find_all('h4')



for movie in moviesUL:
        movie_name = movie.find('a').text
        movie_moreInfo = movie.a['href']

        movieInfoSite = requests.get(f'https://www.imdb.com/{movie_moreInfo}').text
        infoSoup =  BeautifulSoup(movieInfoSite, 'lxml')
        movieRD = infoSoup.find('span', class_ = 'sc-8c396aa2-2 itZqyK').text.replace(' ','')
        print(f'Movie Release Year: {movieRD}')
        print(f'Movie Name: {movie_name}')
        print(f'More Info: https://www.imdb.com/{movie_moreInfo}\n')
