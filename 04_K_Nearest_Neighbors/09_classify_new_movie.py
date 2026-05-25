from movies import movie_dataset, movie_labels, normalize_point
from knn_utils import classify

print("Call Me By Your Name" in movie_dataset)

my_movie = [3500000, 132, 2017]
normalized_my_movie = normalize_point(my_movie)

print("Normalized movie features:", normalized_my_movie)

prediction = classify(normalized_my_movie, movie_dataset, movie_labels, 5)

if prediction == 1:
    print("The movie is predicted to be good.")
else:
    print("The movie is predicted to be bad.")
