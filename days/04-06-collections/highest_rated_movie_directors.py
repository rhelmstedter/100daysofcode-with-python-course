##{
from collections import defaultdict, namedtuple, Counter, deque
import csv
from urllib.request import urlretrieve

# get the data from the web
movie_data = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)
##}

##{
Movie = namedtuple("Movie", "title year score")

def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()
##}


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    for director, movies in directors:
        if len(movies) < MIN_MOVIES:
            directors.pop(director)
        else:
            directors[director].append(_calc_mean(movies))
    return directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum([movie.score for movie in movies])/len(movies), 1)


def print_results(directors, average_scores):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    for director, average_scores in average_scores:
        print()
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    average_scores = get_average_scores(directors)
    print_results(directors, average_scores)


if __name__ == '__main__':
    main()
