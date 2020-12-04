from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def index(request):
    return render(request, 'webbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')
    try:
        movies = pd.read_csv('/home/vika/Downloads/Untitled Folder/Recommended Web/webbot/movies.csv', sep=',', encoding='latin-1', usecols=['movieId','title','genres'])
        tfidf_movies_genres = TfidfVectorizer(token_pattern = '[a-zA-Z0-9\-]+')
        movies['genres'] = movies['genres'].replace(to_replace="(no genres)", value="")
        tfidf_movies_genres_matrix = tfidf_movies_genres.fit_transform(movies['genres'])
        cosine_sim_movies = linear_kernel(tfidf_movies_genres_matrix, tfidf_movies_genres_matrix)
        def get_recommendations_based_on_genres(movie_title, cosine_sim_movies=cosine_sim_movies):
            idx_movie = movies.loc[movies['title'].isin([movie_title])]
            idx_movie = idx_movie.index
            sim_scores_movies = list(enumerate(cosine_sim_movies[idx_movie][0]))
            sim_scores_movies = sorted(sim_scores_movies, key=lambda x: x[1], reverse=True)
            sim_scores_movies = sim_scores_movies[1:3]
            movie_indices = [i[0] for i in sim_scores_movies]
            return movies['title'].iloc[movie_indices]
        
        result = get_recommendations_based_on_genres(query)
        result = result.values.tolist()
        ans = result[0]
        ans1 = result[1]

    except Exception as e:
        ans = "Not Found"
        ans1 = ""
        
    return render(request, 'webbot/index.htm', {'ans': ans, 'ans1': ans1, 'query': query})
