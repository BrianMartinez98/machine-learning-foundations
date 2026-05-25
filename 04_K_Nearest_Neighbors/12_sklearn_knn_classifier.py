from sklearn.neighbors import KNeighborsClassifier
from movies import movie_dataset, movie_labels

classifier = KNeighborsClassifier(n_neighbors=5)

training_points = list(movie_dataset.values())
labels = list(movie_labels.values())

classifier.fit(training_points, labels)

guesses = classifier.predict([
    [0.45, 0.2, 0.5],
    [0.25, 0.8, 0.9],
    [0.1, 0.1, 0.9],
])

print("Predicted classes:", guesses)
