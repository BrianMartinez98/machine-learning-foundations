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
model = LogisticRegression()
cc_lr = model.fit(X_train, y_train)

# Print the intercept and coefficients here:
print("Coefficients:")
print(model.coef_)

print("Intercept:")
print(model.intercept_)
