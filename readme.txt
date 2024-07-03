### README.md

---

# Movie Suggestion App

This project aims to create a movie suggestion app based on user-inputted genres. It involves web scraping data from Box Office Mojo to gather information about top movies across different genres. Users can select a genre, and the app suggests top movies in that genre based on their gross earnings.

## Software and Libraries Used

- Python 3.x
- Requests library for making HTTP requests
- BeautifulSoup (bs4) for parsing HTML content
- Pandas for data manipulation and analysis
- IDE used: (Specify your preferred IDE or text editor)

## Project Structure

- `scrape_movies.py`: Python script for scraping movie data from Box Office Mojo.
- `movie_suggestion.py`: Main script for the movie suggestion app.
- `top_movies.csv`: CSV file to store scraped movie data.

## How to Run

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/movie-suggestion-app.git
   cd movie-suggestion-app
   ```

2. **Install Dependencies:**
   Make sure you have Python installed. Install required libraries using pip:
   ```
   pip install requests beautifulsoup4 pandas
   ```

3. **Run the Scripts:**
   - **Scrape Movies:** Run `scrape_movies.py` to fetch and save movie data.
     ```
     python scrape_movies.py
     ```
     This will create/update `top_movies.csv` with the scraped data.

    **Movie Suggestion App:** Run `movie_suggestion.py` to interactively suggest movies based on genre.
     
     python movie_suggestion.py
     ```
     Follow the prompts to select a genre and view top movie suggestions.

Contributors
-------------

Prakash Tamilathipathi - 
Email - prakatam@amazon.com
