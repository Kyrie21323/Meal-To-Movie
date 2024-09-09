import requests
import random
import pandas as pd
import country_converter as coco
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

TVDB_API_KEY = os.getenv("TVDB_API_KEY")
# TheMealDB API endpoint
MEAL_API_URL = "https://www.themealdb.com/api/json/v1/1/search.php"

# TVDB API endpoint
TVDB_API_URL = "http://api4.thetvdb.com/v4"

def get_meal_info(meal_name):
    params = {"s": meal_name}
    response = requests.get(MEAL_API_URL, params=params)
    data = response.json()
    if data["meals"]:
        return data["meals"][0]
    return None

def get_country_code_from_demonym(demonym):
    # Load demonyms CSV file
    df = pd.read_csv("demonyms.csv")
    country = df[df["Demonym"] == demonym]["Country"].values
    country_code = coco.convert(names=country, to='ISO3')
    return country_code if len(country_code) > 0 else demonym

def get_tvdb_token():
    login_url = f"{TVDB_API_URL}/login"
    response = requests.post(login_url, json={"apikey": TVDB_API_KEY})
    return response.json()["data"]["token"]

def get_movies_by_country(country):
    token = get_tvdb_token()
    headers = {"Authorization": f"Bearer {token}"}
    search_url = f"{TVDB_API_URL}/search"
    params = {
        "query": country,
        "type": "movie",
        "country": country
    }
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    
    if "data" in data and data["data"]:
        suggestion = random.choice(data["data"])
        return suggestion
    return None

def main():
    meal_name = input("Enter a meal name: ")
    meal_info = get_meal_info(meal_name)

    if meal_info:
        area = meal_info["strArea"]   
        country_code = get_country_code_from_demonym(area)
        country = coco.convert(names=country_code, to='name_short')
        print(f"The meal '{meal_name}' is from {country}.")

        movie = get_movies_by_country(country_code)
        if movie:
            print(f"\nHere is a movie suggestion from {country}:")
            print(f"{movie['name']} ({movie['translations']['eng']}, {movie['year']})")
            print()
        else:
            print(f"Sorry, couldn't find any movies from {country}.")
    else:
        print(f"Sorry, couldn't find information for the meal '{meal_name}'.")

if __name__ == "__main__":
    main()