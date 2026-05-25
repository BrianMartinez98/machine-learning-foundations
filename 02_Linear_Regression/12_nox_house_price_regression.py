import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load housing dataset
df = pd.read_csv("nox_house_price_data.csv")

# Set the x-values to the nitrogen oxide concentration:
X = df[["nox"]]

# Y-values are the house prices:
y = df["house_price"]

# Can we do linear regression on this?
line_fitter = LinearRegression()
line_fitter.fit(X, y)

nox_range = np.linspace(X["nox"].min(), X["nox"].max(), 100).reshape(-1, 1)
price_predictions = line_fitter.predict(nox_range)

plt.scatter(X, y, alpha=0.4)

# Plot line here:
plt.plot(nox_range, price_predictions)

plt.title("Nitric Oxides Concentration vs. House Price")
plt.xlabel("Nitric Oxides Concentration")
plt.ylabel("House Price ($1000s)")

plt.savefig("nox_house_price_regression.png", dpi=300, bbox_inches="tight")
plt.show()

print("Intercept:", line_fitter.intercept_)
print("Slope:", line_fitter.coef_[0])
