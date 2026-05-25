from knn_utils import euclidean_distance, manhattan_distance, hamming_distance

print("Euclidean distance:", euclidean_distance([1, 2], [4, 0]))
print("Euclidean distance:", euclidean_distance([5, 4, 3], [1, 7, 9]))

print("Manhattan distance:", manhattan_distance([1, 2], [4, 0]))
print("Manhattan distance:", manhattan_distance([5, 4, 3], [1, 7, 9]))

print("Hamming distance:", hamming_distance([1, 2], [1, 100]))
print("Hamming distance:", hamming_distance([5, 4, 9], [1, 7, 9]))
