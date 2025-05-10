# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 1. keys() - Get all keys
print("Keys:", my_dict.keys())  


# 2. values() - Get all values
print("Values:", my_dict.values())  


# 3. items() - Get all key-value pairs
print("Items:", my_dict.items())  


# 4. get() - Get a value safely
print("Get age:", my_dict.get("age"))  

print("Get gender (default):", my_dict.get("gender", "Not Found"))  

# 5. update() - Update dictionary
my_dict.update({"age": 26, "country": "USA"})
print("After update:", my_dict)  


age = my_dict.pop("age")
print("Popped age:", age)  

print("After pop:", my_dict)  

# 7. popitem() - Remove and return the last item
last_item = my_dict.popitem()
print("Popped item:", last_item)  

print("After popitem:", my_dict)  

# 8. setdefault() - Get value, set default if not present
gender = my_dict.setdefault("gender", "Female")
print("Set default gender:", gender)  
print("After setdefault:", my_dict)  

# 9. clear() - Remove all items
my_dict.clear()
print("After clear:", my_dict)  


# 10. copy() - Create a copy of dictionary
original = {"a": 1, "b": 2}
copy_dict = original.copy()
print("Copied dictionary:", copy_dict)  


# 11. Merge two dictionary
dict1 = {"A": 1, "B": 2, "C": 3}
dict2 = {"D": 4, "E": 5, "F": 6}

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)

