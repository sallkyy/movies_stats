import pandas as pd

df_movies = pd.read_csv("D:/movies/movies_metadata.csv")
print(df_movies.info())
df_movies_new = df_movies[['id','title','budget','revenue','vote_average','popularity','release_date']]

df_movies_new.to_csv(r"D:/movies/movies_data.csv", index=False, sep=",")

print("/n")

df_ratings = pd.read_csv("D:/movies/ratings_small.csv")
print(df_ratings.info())
print(df_ratings.head())

print("/n")

df_links = pd.read_csv("D:/movies/links_small.csv")
print(df_links.info())
print(df_links.head())

'''
import ast
import pandas as pd

df = pd.read_csv("D:/movies/movies_metadata.csv", usecols=['id', 'genres'], low_memory=False)

df = df[df['id'].str.isnumeric()]
df['id'] = df['id'].astype(int)

def extract_genre_objects(raw_str):
    try:
        data = ast.literal_eval(raw_str)
        if isinstance(data, list):
            # Возвращаем список кортежей: [(16, 'Animation'), (35, 'Comedy')]
            return [(item['id'], item['name']) for item in data if 'id' in item and 'name' in item]
    except (ValueError, SyntaxError):
        pass
    return []

df['genre_tuples'] = df['genres'].apply(extract_genre_objects)

exploded = df[['id', 'genre_tuples']].explode('genre_tuples').dropna()

exploded['genre_id'] = exploded['genre_tuples'].apply(lambda x: x[0])
exploded['genre_name'] = exploded['genre_tuples'].apply(lambda x: x[1])

genres_catalog = exploded[['genre_id', 'genre_name']].drop_duplicates().sort_values('genre_id')
genres_catalog.to_csv('genres.csv', index=False)

movie_genres_link = exploded[['id', 'genre_id']].drop_duplicates()
movie_genres_link.columns = ['movie_id', 'genre_id']
movie_genres_link.to_csv('movie_genres.csv', index=False)

print(f"1. Справочник жанров (genres.csv): {len(genres_catalog)} записей")
print(f"2. Связей фильмов с жанрами (movie_genres.csv): {len(movie_genres_link)} записей")
'''