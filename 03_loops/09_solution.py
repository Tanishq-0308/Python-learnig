items = ["apple", "banana", "orange", "apple", "mango"]

unique_value = set()

for item in items:
    if item in unique_value:
        print("Duplicate",item)
        break
    unique_value.add(item)