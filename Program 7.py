
my_list = [10, 5, 23, 45, 8, 12]

largest_number = my_list[0]

for num in my_list:
    if num > largest_number:
        largest_number = num

print("The largest number in the list is:", largest_number)
