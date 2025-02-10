def get_user_input_for_dict():
    user_dict = {}
    while True:
        key = input("Enter key (or press Enter to stop): ").strip()
        if not key:
            break
        value = input(f"Enter value for key '{key}': ").strip()
        user_dict[key] = value
    return user_dict

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)   
    return merged_dict

print("Enter key-value pairs for the first dictionary:")
dict1 = get_user_input_for_dict()

print("\nEnter key-value pairs for the second dictionary:")
dict2 = get_user_input_for_dict()

merged = merge_dicts(dict1, dict2)

print("\nMerged Dictionary:")
for key, value in merged.items():
    print(f"{key}: {value}")
