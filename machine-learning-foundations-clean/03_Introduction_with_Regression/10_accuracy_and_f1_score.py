# Import pandas and the data
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

exam_pass = pd.read_csv("exam_pass_data.csv")

# Separate out X and y
X = exam_pass[["hours_studied", "practice_test"]]
y = exam_pass["passed_exam"]

# Transform X
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=51
)

# Create and fit the logistic regression model here:
cc_lr = LogisticRegression()
cc_lr.fit(X_train, y_train)

# Save and print the predicted outcomes
y_pred = cc_lr.predict(X_test)

print("Predicted classes:")
print(y_pred)

# Print out the true outcomes for the test data
print("\nTrue classes:")
print(y_test.values)

# Print out the confusion matrix
print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))

# Print accuracy here:
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:")
print(accuracy)

# Print F1 score here:
f1 = f1_score(y_test, y_pred)
print("\nF1 score:")
print(f1)
