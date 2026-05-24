# Import libraries and data
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

exam_pass = pd.read_csv("exam_pass_data.csv")

# Fit the logistic regression model
hours_studied = exam_pass[["hours_studied"]]
passed_exam = exam_pass["passed_exam"]

model = LogisticRegression()
model.fit(hours_studied, passed_exam)

# Save intercept and coef
intercept = model.intercept_[0]
coef = model.coef_[0][0]

# Calculate log_odds here
log_odds = intercept + coef * exam_pass["hours_studied"]
print("Log-odds:")
print(log_odds)

# Calculate pred_probability_passing here
pred_probability_passing = np.exp(log_odds) / (1 + np.exp(log_odds))
print("\nPredicted probability of passing:")
print(pred_probability_passing)