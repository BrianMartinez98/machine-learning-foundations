import matplotlib.pyplot as plt
from data import bs_01

iterations = range(len(bs_01))

plt.plot(iterations, bs_01)

plt.xlabel("Iterations")
plt.ylabel("b value")
plt.title("Intercept convergence with learning rate 0.01")

plt.savefig("intercept_convergence_lr_01.png", dpi=300, bbox_inches="tight")
plt.show()
