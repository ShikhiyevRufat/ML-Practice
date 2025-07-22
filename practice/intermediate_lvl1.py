"""
Define a Product class with attributes: name, category, price, and sales.
Generate random sales data using NumPy.
Convert data into a Pandas DataFrame.
Perform data analysis, such as total revenue, average price per category, and best-selling product.
Visualize the data using:
Bar chart (Total Sales per Category)
Pie chart (Revenue Share per Product)
Line plot (Sales Trend over Months)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, category, price, sales):
        self.name = name
        self.category = category
        self.price = price
        self.sales = sales

    def total_revenue(self):
        return self.price * self.sales


a = np.random.randint(1, 100, 5)

datas = [
    Product("Laptop", "Electronics", 1200, a[0]),
    Product("Phone", "Electronics", 800, a[1]),
    Product("T-shirt", "Clothing", 25, a[2]),
    Product("Shoes", "Clothing", 50, a[3]),
    Product("Headphones", "Electronics", 100, a[4])
]

df = pd.DataFrame([vars(data) for data in datas])

a = [i.total_revenue() for i in datas]
print(a)

avarage_price = df.groupby("category")['price'].mean()

total_sales = df.groupby('category')['sales'].sum()

plt.subplot(1,2,1)

plt.bar(total_sales.index, total_sales.values, color = 'blue')

plt.subplot(1,2,2)

plt.pie([i.total_revenue() for i in datas], labels = df['name'], autopct='%1.1f%%')

plt.show()
