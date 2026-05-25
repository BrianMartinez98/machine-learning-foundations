from movies import training_set, training_labels, validation_set, validation_labels
from knn_utils import classify

print("Bee Movie features:", validation_set["Bee Movie"])
print("Bee Movie true label:", validation_labels["Bee Movie"])

guess = classify(validation_set["Bee Movie"], training_set, training_labels, 5)
print("Predicted label:", guess)

if guess == validation_labels["Bee Movie"]:
    print("Correct!")
else:
    print("Wrong!")
