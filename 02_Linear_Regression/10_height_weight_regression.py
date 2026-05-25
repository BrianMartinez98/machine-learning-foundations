from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

plt.plot(X, y, "o")

b, m = gradient_descent(X, y, num_iterations=1000, learning_rate=0.0001)

y_predictions = [m * x + b for x in X]

plt.plot(X, y_predictions)

plt.title("Height vs. Weight Linear Regression")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.savefig("height_weight_regression.png", dpi=300, bbox_inches="tight")
plt.show()

print("Final intercept:", b)
print("Final slope:", m)
