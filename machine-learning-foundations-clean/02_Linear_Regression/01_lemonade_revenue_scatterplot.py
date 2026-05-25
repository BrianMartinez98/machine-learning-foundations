import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

plt.plot(months, revenue, "o")

plt.title("Sandra's Lemonade Stand")

plt.xlabel("Months")
plt.ylabel("Revenue ($)")

plt.savefig("lemonade_revenue_scatterplot.png", dpi=300, bbox_inches="tight")
plt.show()

# What do you think the revenue in month 13 would be?
month_13 = 195
print("Estimated revenue in month 13:", month_13)
