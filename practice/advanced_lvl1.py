"""
Objective: Build a Python-based E-Commerce Data Analysis System that processes sales data, 
generates reports, and visualizes insights using OOP, NumPy, Pandas, and Matplotlib.
"""
import numpy as np
import pandas as pd
import matplotlib as plt
class Product:
    def __init__(self, name, category, price, sales, rating):
        self.name = name
        self.category = category
        self.price = price
        self.sales = sales
        self.rating = rating

    def __str__(self):
        return f"{self.name} | {self.category} | ${self.price} | Sales: {self.sales} | Rating: {self.rating}"


class Store:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def update_product(self, name, sales):
        for i in self.products:
            if i.name == name:
                i.sales = sales
                return True
        return False
    
    def display_products(self):
        print("\n📌 Product List:")
        for product in self.products:
            print(product)



categories = ["Electronics", "Clothing", "Home Appliances"]
product_names = ["Laptop", "Smartphone", "T-shirt", "Washing Machine", "Headphones", "Sneakers", "Microwave"]
num_products = len(product_names)

sales = np.random.randint(1, 500, num_products)
prices = np.random.randint(10,5000, num_products)
rating = np.random.randint(1, 5, num_products)


store = Store()

for i in range(len(product_names)):
    categorie = np.random.choice(categories)
    products = Product(product_names[i], categorie, prices[i], sales[i], rating[i])
    store.add_product(products)


df = pd.DataFrame([vars(p) for p in store.products])

avarage_price = df.groupby('category')['price'].mean()

print(f"📊 Avarage price per category {avarage_price}")

best_selling = df.loc[df['sales'].idxmax()]

print(f"📈 Top-selling product. {best_selling}")

print(df)

