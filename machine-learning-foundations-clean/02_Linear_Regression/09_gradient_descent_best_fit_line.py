import matplotlib.pyplot as plt
from data import months, revenue, gradient_descent

# Run gradient descent
b, m = gradient_descent(months, revenue, learning_rate=0.01, num_iterations=1000)

# Generate predicted values using the final line
y_predicted = [m * x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y_predicted)

plt.title("Best fit line using gradient descent")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")

plt.savefig("gradient_descent_best_fit_line.png", dpi=300, bbox_inches="tight")
plt.show()

print("Final intercept:", b)
print("Final slope:", m)
