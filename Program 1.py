def sort_dict_by_value(d, ascending=True):
   
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))
    return sorted_dict


my_dict = {'Car': 3, 'Bus': 1, 'Truck': 2, 'Aeroplane': 5}


ascending_sorted_dict = sort_dict_by_value(my_dict, ascending=True)
print("Sorted in ascending order:")
print(ascending_sorted_dict)


descending_sorted_dict = sort_dict_by_value(my_dict, ascending=False)
print("\nSorted in descending order:")
print(descending_sorted_dict)
