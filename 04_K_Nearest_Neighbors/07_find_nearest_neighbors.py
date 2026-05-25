from movies import movie_dataset, movie_labels
from knn_utils import find_neighbors

# print(movie_dataset["Bruce Almighty"])
# print(movie_labels["Bruce Almighty"])

neighbors = find_neighbors([0.4, 0.2, 0.9], movie_dataset, 5)

print("Five nearest neighbors:")
print(neighbors)
