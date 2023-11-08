def key_exists_in_dict(key, my_dict):
  
    if key in my_dict:
        return True
    else:
        return False


my_dict = {'Car': 3, 'Bus': 1, 'Truck': 2, 'Aeroplane': 5}


key_to_check = 'Bus'


if key_exists_in_dict(key_to_check, my_dict):
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")


if my_dict.get(key_to_check) is not None:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")
