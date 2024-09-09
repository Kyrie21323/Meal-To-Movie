# Projects in programming and data science
## Activity 1 - Data Feature (meal-to-movie matching program)

Ziyue and I came up with the idea of suggesting a movie to watch which would be related to what that person is eating. We named it "meal-to-movie matching program". This program basically suggests a movie based on the meal a user inputs. It uses TheMealDB API to retrieve information about the meal, including its country of origin, and the TVDB API to find a movie related to that country. The country is converted to an ISO3 code using the `country_converter` library, which is then used to search for a random movie. The movie’s name, release year, and an English translation (if available) are displayed to the user, and if the movie has a thumbnail, it is fetched and displayed using `matplotlib` and `PIL`. If no meal or movie information is found, the program informs the user, handling missing data. The program is interactive and visually engaging, enhancing the dining experience with a relevant movie suggestion.

*The details on coding is written on google collab.*
