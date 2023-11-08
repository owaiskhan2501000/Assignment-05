
my_array = [1, 2, 3, 4, 5]


print("Array items:", my_array)

index = 3  

if 0 <= index < len(my_array):
    element = my_array[index]
    print(f"Element at index {index} is {element}")
else:
    print(f"Index {index} is out of range. The array has {len(my_array)} elements.")
