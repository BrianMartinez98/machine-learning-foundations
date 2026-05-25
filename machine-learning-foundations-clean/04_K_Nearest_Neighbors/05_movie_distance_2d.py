star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]


def distance(movie1, movie2):
    length_difference = (movie1[0] - movie2[0]) ** 2
    year_difference = (movie1[1] - movie2[1]) ** 2
    final_distance = (length_difference + year_difference) ** 0.5
    return final_distance


print("Star Wars to Raiders:", distance(star_wars, raiders))
print("Star Wars to Mean Girls:", distance(star_wars, mean_girls))
