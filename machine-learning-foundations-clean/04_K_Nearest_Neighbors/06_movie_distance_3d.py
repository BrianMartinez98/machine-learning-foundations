from knn_utils import euclidean_distance

star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

print("Star Wars to Raiders:", euclidean_distance(star_wars, raiders))
print("Star Wars to Mean Girls:", euclidean_distance(star_wars, mean_girls))
