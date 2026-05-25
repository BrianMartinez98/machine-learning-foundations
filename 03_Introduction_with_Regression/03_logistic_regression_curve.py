import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

exam_pass = pd.read_csv("exam_pass_data.csv")

# Fit the logistic regression model
hours_studied = exam_pass[["hours_studied"]]
passed_exam = exam_pass["passed_exam"]

model = LogisticRegression()
model.fit(hours_studied, passed_exam)

# Define five_hour_studier below
five_hour_studier = model.predict_proba([[5]])[0][1]
print("Probability of passing after studying 5 hours:", five_hour_studier)

# Plug sample data into fitted model
sample_x = np.linspace(-1, 25, 300).reshape(-1, 1)
probability = model.predict_proba(sample_x)[:, 1]

# Plot exam data
plt.scatter(hours_studied, passed_exam, color="black", s=100)

# Plot logistic curve
plt.plot(sample_x, probability, color="red", linewidth=3)

# Customization for readability
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=1, color="black", linestyle="--")

# Label plot and set limits
plt.ylabel("probability passed", fontsize=15)
plt.xlabel("hours studied", fontsize=15)
plt.xlim(-1, 25)
plt.tight_layout()

# Show the plot
plt.savefig("logistic_regression_curve.png", dpi=300, bbox_inches="tight")
plt.show()
