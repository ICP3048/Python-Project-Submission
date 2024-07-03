import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape top movies from Box Office Mojo with genre
def scrape_top_movies_with_genre():
    try:
        url = "https://www.boxofficemojo.com/genre/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        print(f"Request status code: {response.status_code}")
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.content, 'html.parser')
        movies = []

        movie_items = soup.find_all('tr')

        for item in movie_items[1:]: 
            columns = item.find_all('td')
            title = columns[3].text.strip()
            gross = columns[1].text.strip()
            genre = columns[0].text.strip()
            movies.append({'title': title, 'gross': gross, 'genre': genre})
            print(f"Scraped movie: {title}, Gross: {gross}, Genre: {genre}")

        return movies

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return []
    except Exception as e:
        print(f"Error occurred during scraping: {e}")
        return []

# Saving to CSV
def save_movies_to_csv(movies, filename="movies.csv"):
    try:
        if movies:
            df = pd.DataFrame(movies)
            df.to_csv(filename, index=False)
            print(f"Movies data saved to {filename} successfully.")
        else:
            print("No movies to save.")
    except Exception as e:
        print(f"Error occurred while saving to CSV: {e}")

def suggest_top_movies_by_genre(genre, movies):
    filtered_movies = [movie for movie in movies if genre.lower() in movie['genre'].lower()]
    sorted_movies = sorted(filtered_movies, key=lambda x: float(x['gross'].replace('$', '').replace(',', '')), reverse=True)[:5]

    return sorted_movies

if __name__ == "__main__":
    movies_data = scrape_top_movies_with_genre()
    if movies_data:
        save_movies_to_csv(movies_data, filename="top_movies.csv")
    else:
        print("No data scraped, nothing to save.")
    try:
        df = pd.read_csv("top_movies.csv")
    except FileNotFoundError:
        print("CSV file not found. Please run the scraping function first.")
        df = pd.DataFrame()
    if not df.empty:
        genres = df['genre'].unique().tolist()
        print("Available genres:")
        for i, genre in enumerate(genres, start=1):
            print(f"{i}. {genre}")
        
        while True:
            genre_choice = input("Enter the number of the genre to search (e.g., 1 for Heroine): ").strip()

            try:
                genre_index = int(genre_choice) - 1
                selected_genre = genres[genre_index]
                print(f"Searching for top 5 movies in {selected_genre}...")
                suggested_movies = suggest_top_movies_by_genre(selected_genre, df.to_dict('records'))
                if suggested_movies:
                    print(f"\nTop 5 {selected_genre} movies based on gross collections:")
                    for i, movie in enumerate(suggested_movies, start=1):
                        print(f"{i}. {movie['title']} - Gross: {movie['gross']}")
                else:
                    print(f"No {selected_genre} movies found.")
                
                choice = input("\nDo you want to search for another genre? (yes/no): ").strip().lower()
                if choice != 'yes':
                    break 

            except (IndexError, ValueError):
                print("Invalid genre selection. Please enter a valid number from the list.")
    else:
        print("No movies data available.")
