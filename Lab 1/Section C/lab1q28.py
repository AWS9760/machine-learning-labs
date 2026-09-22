import matplotlib
import matplotlib.pyplot as plt
import numpy as np


subjects = ["Math", "Science", "English", "History"]
avg_marks = [78, 92, 84, 69]
colors = ["skyblue"] * len(subjects)
colors[int(np.argmax(avg_marks))] = "gold"
plt.figure(figsize=(7, 4))
plt.bar(subjects, avg_marks, color=colors)
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.savefig("q28_bar_chart.png", dpi=150)
plt.show()
plt.close()