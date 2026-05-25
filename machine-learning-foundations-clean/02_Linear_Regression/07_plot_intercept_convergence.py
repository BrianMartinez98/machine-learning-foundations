import matplotlib.pyplot as plt
from data import bs

iterations = range(len(bs))

plt.plot(iterations, bs)

plt.xlabel("Iterations")
plt.ylabel("b value")
plt.title("Convergence of intercept b")

plt.savefig("intercept_convergence.png", dpi=300, bbox_inches="tight")
plt.show()

convergence_b = 47
num_iterations = 800

print("Approximate convergence value for b:", convergence_b)
print("Approximate number of iterations:", num_iterations)
