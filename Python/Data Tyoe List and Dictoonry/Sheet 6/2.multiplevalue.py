data = {}
while True:
    key = input("Enter key (or 'stop' to end): ")
    if key.lower() == 'stop':
        break
    value = input("Enter value: ")
    if key in data:
        if isinstance(data[key], list):
            data[key].append(value)
        else:
            data[key] = [data[key], value]
    else:
        data[key] = [value]
print(data)
