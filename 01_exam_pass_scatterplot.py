import codecademylib3
import pandas as pd
import matplotlib.pyplot as plt
exam_pass = pd.read_csv('exam_pass_data.csv')

# Scatter plot of exam passage vs number of hours studied
plt.scatter(x = 'hours_studied', y = 'passed_exam', data = codecademyU, color='black')
plt.ylabel('passed/failed')
plt.xlabel('hours studied')

plt.show()
