import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv("students.csv")

print("Dataset:")
print(data)

# Average marks
print("\nAverage Marks:")
print(data[['Maths', 'Science', 'English']].mean())

# Maximum marks
print("\nMaximum Marks:")
print(data[['Maths', 'Science', 'English']].max())

# Minimum marks
print("\nMinimum Marks:")
print(data[['Maths', 'Science', 'English']].min())

# Bar chart
data.set_index("Name")[['Maths', 'Science', 'English']].plot(kind='bar')
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Scatter plot
plt.scatter(data['Maths'], data['Science'])
plt.title("Maths vs Science Marks")
plt.xlabel("Maths")
plt.ylabel("Science")
plt.show()

# Heatmap
sns.heatmap(data[['Maths', 'Science', 'English']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
