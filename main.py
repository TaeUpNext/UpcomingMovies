# sourcery skip: hoist-similar-statement-from-if, hoist-statement-from-if
from bs4 import BeautifulSoup
import requests
import re
from datetime import date
from pathlib import Path

#gets the current path for the file to be able to work with it
p = Path(__file__)
dir_abs = p.parent.absolute()

today = date.today()

html_site = requests.get('https://www.imdb.com/calendar/').text #the site were getting the info from

soup = BeautifulSoup(html_site, 'lxml')


#movies = soup.find_all('div', id=re.compile('^main'))
moviesDiv = soup.find('div', id = 'main')
moviesUL = moviesDiv.find_all('li') #finds all li elements in the div group wiht the id of main
moviesReleaseDate = moviesDiv.find_all('h4') #h4 

print("Getting Upcoming Movies.....\n")
with open(f'{dir_abs}/movies/Updated Movies as of {today}.txt', 'w') as f: #opens the current directory enters movie folder and opens or creates the file to be written too
    for movie in moviesUL: #loop to go through all
        movie_name = movie.find('a').text
        movie_moreInfo = movie.a['href']

        movieInfoSite = requests.get(f'https://www.imdb.com/{movie_moreInfo}').text #requests to get information from the movies IMBD page
        infoSoup =  BeautifulSoup(movieInfoSite, 'lxml')
        movieRD = infoSoup.find('span', class_ = 'sc-8c396aa2-2 itZqyK').text.replace(' ','') #this gets the year the movie comes out from the more info page because this is saved in a span element with the class id as displayed
        expectedDate = infoSoup.find('div', class_ = 'sc-5766672e-2 bweBzH') #finds the expected date this item is saved in a div with the class id as displayed

        if expectedDate is None:
            expectedDate = 'N/A'
            f.write(f'Movie Name: {movie_name}\n')
            f.write(f'Movie Release Year: {movieRD}\n')
            f.write(f'Expected Release Date: {expectedDate}\n')
            f.write(f'More Info: https://www.imdb.com/{movie_moreInfo}\n\n')

        else:
            expectedDate = infoSoup.find('div', class_ = 'sc-5766672e-2 bweBzH').text.replace('Releases','')
            f.write(f'Movie Name: {movie_name}\n')
            f.write(f'Movie Release Year: {movieRD}\n')
            f.write(f'Expected Release Date: {expectedDate}\n')
            f.write(f'More Info: https://www.imdb.com/{movie_moreInfo}\n\n')
    print('\nYour File has been saved')
