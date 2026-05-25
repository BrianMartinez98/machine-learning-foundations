from movies import movie_dataset, movie_labels
from knn_utils import classify

prediction = classify([0.4, 0.2, 0.9], movie_dataset, movie_labels, 5)

if prediction == 1:
    print("The unknown movie is predicted to be good.")
else:
    print("The unknown movie is predicted to be bad.")

print("Predicted class:", prediction)
