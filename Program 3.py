def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary using dictionary unpacking:", merged_dict)
