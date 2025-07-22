"""
Create a simple line plot with x = [1, 2, 3, 4, 5] and y = [10, 20, 25, 30, 40].
Label the x-axis as "X Values" and y-axis as "Y Values".
Add a title: "Simple Line Plot".
"""

import matplotlib.pyplot as plt
import numpy as np


# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# plt.plot(x, y, linestyle = '-', marker = 'o', label = 'Growth', color = "red")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("Simple Line Plot")
# plt.show()

"""
Plot two different lines on the same figure with labels.
Use different colors (red and blue) and line styles (dashed and solid).
Add a legend.
"""

# x1 = [1, 2, 3, 4, 5]
# y1 = [10, 20, 25, 30, 40]

# x2 = [6, 7, 8, 9, 10]
# y2 = [15, 25, 35, 45, 55]

# plt.plot(x1, y1, linestyle = 'dashed', marker = 'o', color = 'red', label = 'line1')
# plt.plot(x2, y2, linestyle = 'solid', marker = 'o', color = 'blue', label = 'line2')

# plt.xlabel("X Values")
# plt.ylabel("Y Values")
# plt.title("Two Lines on One Plot")

# plt.legend()
# plt.show()

"""
Generate random x and y values using numpy.random and create a scatter plot.
Change the marker size and color.
"""

# arr_x = np.random.randint(1,100, 20)
# arr_y = np.random.randint(1,100, 20)
# sizes = np.random.randint(1,100, 20)

# plt.scatter(arr_x, arr_y, color = "red", s = sizes, label = "Arrays")

# plt.legend()
# plt.show()

"""
Plot a bar chart for sales data.
Change bar colors and add value labels on top of each bar.
"""
# categories = ['A', 'B', 'C', 'D']
# values = [10, 15, 7, 12]


# plt.bar(categories, values, color = "blue")
# for i, value in enumerate(values):
#     plt.text(i, value, str(value), ha='center', fontsize=12, fontweight='bold')

# plt.show()

"""
Generate 1000 random values from a normal distribution and plot a histogram.
Set bins=30, use transparency (alpha=0.7).
"""

# arr = np.random.normal(loc=0, scale=1, size=1000)
# plt.hist(arr, bins=30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
# plt.show()

"""
Subplots
Create two subplots:
The first plot shows a line plot.
The second plot shows a bar chart.
Use plt.subplot() to arrange them in a 1x2 grid.
"""

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 30, 25, 40]

# categories = ["A", "B", "C", "D", "E"]
# values = [150, 200, 250, 180, 220]

# plt.figure(figsize=(12, 5)) 

# plt.subplot(1,2,1)
# plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Line Data")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Line Plot")
# plt.legend()

# plt.subplot(1,2,2)
# plt.bar(categories, values, color = 'green')
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Bar Chart")

# plt.tight_layout() 
# plt.show()

"""
Plot a pie chart using sales data:
Add a legend and display percentage values.
"""

# labels = ['Product A', 'Product B', 'Product C', 'Product D']
# sizes = [35, 30, 20, 15]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.legend(labels, title = 'Products', loc = "best")
# plt.show()

"""
Create a box plot for a dataset with random numbers.
Label the axes and title the plot.
"""

# data = np.random.randint(10, 100, 50) 

# plt.boxplot(data, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# plt.show()

"""
Stacked Bar Chart
Plot a stacked bar chart showing quarterly revenue from multiple products.
"""

# quarters = ["Q1", "Q2", "Q3", "Q4"]
# product_A = [30, 40, 50, 45] 
# product_B = [20, 35, 40, 30] 
# product_C = [25, 30, 35, 40]  

# plt.bar(quarters, product_A, color='blue', label="Product A")
# plt.bar(quarters, product_B, bottom=product_A, color='green', label="Product B")
# plt.bar(quarters, product_C, bottom=np.array(product_A) + np.array(product_B), color='red', label="Product C")

# plt.xlabel("Quarters")
# plt.ylabel("Revenue (in millions)")
# plt.title("Quarterly Revenue by Product")
# plt.legend()

# plt.show()