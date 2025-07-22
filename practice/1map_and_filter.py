words = ["apple", "banana", "cherry", "date", "fig"]


a = lambda x: "e" in x

b = list(filter(a, words))
print(b)