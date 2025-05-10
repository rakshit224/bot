# Empty list
my_list = []

# List with elements
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# Using index (starts from 0)
print(numbers[0])   # 10
print(fruits[2])    # cherry

# Negative indexing
print(numbers[-1])  # 40 (last element)

# Change an element
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Add elements
fruits.append("date")             # Add to end
fruits.insert(1, "banana")        # Insert at index 1
print(fruits)

# Remove elements
fruits.remove("apple")            # Remove by value
last = fruits.pop()               # Remove and return last item
print(fruits)
