from scipy.spatial import distance
from knn_utils import euclidean_distance, manhattan_distance, hamming_distance

print("Manual Euclidean distance:", euclidean_distance([1, 2], [4, 0]))
print("Manual Manhattan distance:", manhattan_distance([1, 2], [4, 0]))
print("Manual Hamming distance:", hamming_distance([5, 4, 9], [1, 7, 9]))

print("SciPy Euclidean distance:", distance.euclidean([1, 2], [4, 0]))
print("SciPy Manhattan distance:", distance.cityblock([1, 2], [4, 0]))
print("SciPy Hamming distance:", distance.hamming([5, 4, 9], [1, 7, 9]))
