# Data Feature (meal-to-movie matching program)

Ziyue and I came up with the idea of suggesting a movie to watch which would be related to what that person is eating. We named it "meal-to-movie matching program". This program basically suggests a movie based on the meal a user inputs. It uses TheMealDB API to retrieve information about the meal, including its country of origin, and the TVDB API to find a movie related to that country. The country is converted to an ISO3 code using the `country_converter` library, which is then used to search for a random movie. The movie’s name, release year, and an English translation (if available) are displayed to the user, and if the movie has a thumbnail, it is fetched and displayed using `matplotlib` and `PIL`. If no meal or movie information is found, the program informs the user, handling missing data. The program is interactive and visually engaging, enhancing the dining experience with a relevant movie suggestion.

*The details on coding is written on google collab.*



## How to Run the Project

1. Ensure you have Python (Python 3.12 used for development) installed on your system.

2. Clone this repository to your local machine.

   ```
   git clone https://github.com/ZYTao12/data-feature.git
   cd data-feature
   ```

3. Install the required dependencies. You may need to install additional libraries. Use pip to install any missing dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables (you will need to create an account to get the TVDB API key).

   ```
   touch .env
   echo TVDB_API_KEY=your_tvdb_api_key >> .env
   ```

5. Run the main script:

   ```
   python meal_with_movie.py
   ```

6. When prompted, enter a meal name.

7. The application will display information about the meal's origin and suggest a movie from the same country.

## Example

Please refer to Assignment_01_Data_Features.ipynb.
