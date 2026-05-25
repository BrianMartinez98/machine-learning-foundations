from knn_utils import min_max_normalize

# Synthetic movie data: title -> [budget, runtime, release_year, imdb_rating]
# The label is 1 for rating >= 7.0 and 0 otherwise.
raw_movies = {
    "Star Wars": [11000000, 125, 1977, 8.6],
    "Raiders of the Lost Ark": [18000000, 115, 1981, 8.4],
    "Mean Girls": [17000000, 97, 2004, 7.1],
    "The Shining": [19000000, 146, 1980, 8.4],
    "Gone with the Wind": [3977000, 238, 1939, 8.2],
    "Finding Nemo": [94000000, 100, 2003, 8.2],
    "Superman II": [54000000, 127, 1980, 6.8],
    "Blazing Saddles": [2600000, 93, 1974, 7.7],
    "Bruce Almighty": [81000000, 101, 2003, 6.8],
    "Bee Movie": [150000000, 91, 2007, 6.1],
    "Akira": [5500000, 124, 1988, 8.0],
    "Godzilla 2000": [8300000, 99, 1999, 6.1],
    "Lady Vengeance": [4200000, 115, 2005, 7.5],
    "Steamboy": [20000000, 126, 2004, 6.8],
    "Toy Story": [30000000, 81, 1995, 8.3],
    "The Room": [6000000, 99, 2003, 3.6],
    "Casablanca": [878000, 102, 1942, 8.5],
    "Jaws": [9000000, 124, 1975, 8.1],
    "Avatar": [237000000, 162, 2009, 7.9],
    "Cats": [95000000, 110, 2019, 2.8],
}

budgets = [movie[0] for movie in raw_movies.values()]
runtimes = [movie[1] for movie in raw_movies.values()]
years = [movie[2] for movie in raw_movies.values()]

normalized_budgets = min_max_normalize(budgets)
normalized_runtimes = min_max_normalize(runtimes)
normalized_years = min_max_normalize(years)

movie_dataset = {}
movie_labels = {}

for index, title in enumerate(raw_movies):
    movie_dataset[title] = [
        normalized_budgets[index],
        normalized_runtimes[index],
        normalized_years[index],
    ]
    movie_labels[title] = 1 if raw_movies[title][3] >= 7.0 else 0

labels = list(movie_labels.values())

# Simple validation split.
validation_titles = ["Bee Movie", "The Room", "Avatar", "Toy Story"]
training_titles = [title for title in movie_dataset if title not in validation_titles]

training_set = {title: movie_dataset[title] for title in training_titles}
training_labels = {title: movie_labels[title] for title in training_titles}
validation_set = {title: movie_dataset[title] for title in validation_titles}
validation_labels = {title: movie_labels[title] for title in validation_titles}


def normalize_point(point):
    budget, runtime, year = point

    normalized_budget = (budget - min(budgets)) / (max(budgets) - min(budgets))
    normalized_runtime = (runtime - min(runtimes)) / (max(runtimes) - min(runtimes))
    normalized_year = (year - min(years)) / (max(years) - min(years))

    return [normalized_budget, normalized_runtime, normalized_year]
