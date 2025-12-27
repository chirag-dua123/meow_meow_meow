import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#Line plot
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o')        #marker shows the data points
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('My First Customized Plot')
plt.grid(True)      #this shows a grid on the graph
plt.show()      #this is to show the graph, other commands just make the graph but this one shows it

# Scatter plot
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, alpha=0.5, c='blue', s=50)
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
plt.bar(categories, values)
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.show()