# Import pandas and the data
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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
    random_state=27
)

# Create and fit the logistic regression model here:
cc_lr = LogisticRegression()
cc_lr.fit(X_train, y_train)

# Print out the predicted outcomes for the test data
print("Predicted outcomes:")
print(cc_lr.predict(X_test))

# Print out the predicted probabilities for the test data
print("\nPredicted probabilities:")
print(cc_lr.predict_proba(X_test))

# Print out the true outcomes for the test data
print("\nTrue outcomes:")
print(y_test.values)
