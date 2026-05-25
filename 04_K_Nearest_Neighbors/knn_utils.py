def check_same_dimension(pt1, pt2):
    if len(pt1) != len(pt2):
        raise ValueError("Points must have the same number of dimensions.")


def euclidean_distance(pt1, pt2):
    check_same_dimension(pt1, pt2)

    distance = 0
    for i in range(len(pt1)):
        distance += (pt1[i] - pt2[i]) ** 2

    return distance ** 0.5


def manhattan_distance(pt1, pt2):
    check_same_dimension(pt1, pt2)

    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])

    return distance


def hamming_distance(pt1, pt2):
    check_same_dimension(pt1, pt2)

    distance = 0
    for i in range(len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1

    return distance


def min_max_normalize(values):
    minimum = min(values)
    maximum = max(values)

    if maximum == minimum:
        return [0 for _ in values]

    normalized = []
    for value in values:
        normalized_value = (value - minimum) / (maximum - minimum)
        normalized.append(normalized_value)

    return normalized


def find_neighbors(unknown, dataset, k):
    distances = []

    for title in dataset:
        point = dataset[title]
        distance_to_point = euclidean_distance(point, unknown)
        distances.append([distance_to_point, title])

    distances.sort()
    neighbors = distances[:k]

    return neighbors


def classify(unknown, dataset, labels, k):
    neighbors = find_neighbors(unknown, dataset, k)

    num_good = 0
    num_bad = 0

    for neighbor in neighbors:
        title = neighbor[1]

        if labels[title] == 0:
            num_bad += 1
        elif labels[title] == 1:
            num_good += 1

    if num_good > num_bad:
        return 1
    return 0


def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
    num_correct = 0.0

    for title in validation_set:
        guess = classify(validation_set[title], training_set, training_labels, k)

        if guess == validation_labels[title]:
            num_correct += 1

    return num_correct / len(validation_set)
