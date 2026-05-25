from movies import training_set, training_labels, validation_set, validation_labels
from knn_utils import find_validation_accuracy

for k in range(1, 10):
    accuracy = find_validation_accuracy(
        training_set,
        training_labels,
        validation_set,
        validation_labels,
        k,
    )
    print(f"k={k}: validation accuracy={accuracy:.2f}")
