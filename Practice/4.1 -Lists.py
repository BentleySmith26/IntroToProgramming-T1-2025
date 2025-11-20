Store = ["Grape", "Apple", "Banana", "Orange", "Pear"]
print(Store)

print(f"The first fruit in the list is '{Store[0]}'.")
print(f"The last fruit in the list is '{Store[-1]}'.")

x = input("Please input a new fruit\n> ")
Store.append(x)
print(Store)

y = input("Please input which fruit you want to remove\n> ")
Store.remove(y)
print(Store)

Store.sort()
print(Store)

Store_two = ["apple", "banana", "apple", "orange", "banana"]
print(Store_two)
print(f"There are {Store_two.count("apple")} instances of 'apple'")

for fruit in Store:
    print(fruit)


