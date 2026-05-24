import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

exam_pass = pd.read_csv("exam_pass_data.csv")

# Define slacker, average, and studious below
slacker = -0.2
average = 0.5
studious = 1.75

# Fit a linear model
model = LinearRegression()
model.fit(exam_pass[["hours_studied"]], exam_pass[["passed_exam"]])

# Get predictions from the linear model
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1, 1)
predictions = model.predict(sample_x)

# Plot the data
plt.scatter(
    x="hours_studied",
    y="passed_exam",
    data=exam_pass,
    color="black",
    s=100
)

# Plot the line
plt.plot(sample_x, predictions, color="red", linewidth=3)

# Customization for readability
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.axhline(y=0, color="black", linestyle="--")
plt.axhline(y=1, color="black", linestyle="--")

# Label plot and set limits
plt.ylabel("outcome (1=passed, 0=failed)", fontsize=15)
plt.xlabel("hours studied", fontsize=15)
plt.xlim(-16.65, 33.35)
plt.ylim(-0.3, 1.8)

# Show the plot
plt.tight_layout()
plt.savefig("linear_regression_approach.png", dpi=300, bbox_inches="tight")
plt.show()
