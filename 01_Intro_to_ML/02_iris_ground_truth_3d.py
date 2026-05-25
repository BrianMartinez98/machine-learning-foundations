import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

# Plot the ground truth
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection="3d", elev=48, azim=134)

for name, label in [
    ("Robots", 0),
    ("Cyborgs", 1),
    ("Humans", 2)
]:
    ax.text3D(
        x[y == label, 3].mean(),
        x[y == label, 0].mean(),
        x[y == label, 2].mean() + 2,
        name,
        horizontalalignment="center",
        bbox=dict(alpha=0.2, edgecolor="white", facecolor="white")
    )

# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(float)

ax.scatter(
    x[:, 3],
    x[:, 0],
    x[:, 2],
    c=y,
    edgecolor="black"
)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.set_xlabel("Time to Heal")
ax.set_ylabel("Reading Speed")
ax.set_zlabel("EQ")

ax.set_title("Iris dataset ground truth")

plt.tight_layout()
plt.savefig("iris_ground_truth_3d.png", dpi=300, bbox_inches="tight")
plt.show()
