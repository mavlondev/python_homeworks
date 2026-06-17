# ## Task 1: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the `requests` library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

# ## Task 2: Movie Recommendation System
#    1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.
import requests
import random

# Task 1: Weather API
def get_weather(city):
    api_key = 'your_api_key'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Error fetching weather data")

# Task 2: Movie Recommendation System
def get_movie_recommendation(genre):
    api_key = 'your_api_key'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['title']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found for this genre")
    else:
        print("Error fetching movie data")
if __name__ == "__main__":
    city = input("Enter a city to get weather information: ")
    get_weather(city)

    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    get_movie_recommendation(genre)

