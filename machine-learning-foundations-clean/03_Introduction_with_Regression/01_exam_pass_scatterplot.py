import pandas as pd
import matplotlib.pyplot as plt

exam_pass = pd.read_csv("exam_pass_data.csv")

plt.scatter(
    x="hours_studied",
    y="passed_exam",
    data=exam_pass,
    color="black"
)

plt.ylabel("passed/failed")
plt.xlabel("hours studied")
plt.title("Exam outcome vs. hours studied")

plt.savefig("exam_pass_scatterplot.png", dpi=300, bbox_inches="tight")
plt.show()
