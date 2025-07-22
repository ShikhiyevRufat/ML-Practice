# OOP, Numpy, Pandas, Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    

products = [
    Product("Laptop", "Electronics", 1200),
    Product("Phone", "Electronics", 800),
    Product("T-shirt", "Clothing", 25),
    Product("Shoes", "Clothing", 50),
    Product("Headphones", "Electronics", 100)
]

df = pd.DataFrame([vars(p) for p in products])

avara_price = np.mean(df['price'])

plt.bar(df['name'],df["price"], color = "red")

plt.show()