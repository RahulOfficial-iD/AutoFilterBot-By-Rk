from imdb import IMDb

ia = IMDb()

async def get_movie_details(query):
    movies = ia.search_movie(query)
    if not movies:
        return {}
    
    movie = movies[0]
    ia.update(movie)
    return {
        "title": movie.get('title'),
        "rating": movie.get('rating'),
        "poster": movie.get('full-size cover url'),
        "genres": movie.get('genres')
    }
