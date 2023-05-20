import pandas as pd
import matplotlib.pyplot as plt

years = list(range(2011, 2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {"years": years, "durations": durations}
durations_df = pd.DataFrame(movie_dict)

plt.plot(years, durations)
plt.title("Netflix Movie Durations 2011-2020")
plt.xlabel("Year")
plt.ylabel("Duration (min)")
plt.show()

netflix_df = pd.read_csv("netflix_data.csv")
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]

short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]

colors = []
for _, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == "Children":
        colors.append("red")
    elif row['genre'] == "Documentaries":
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (min)")
plt.show()
