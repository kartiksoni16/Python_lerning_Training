Lst = [
    {52: {'march': 1, 'may': 2, 'june': 3, 'july': 1, 'feb': 0, 'aug': 2, 'jan': 0, 'april': 5, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
    {52: {'march': 0, 'may': 0, 'june': 0, 'july': 0, 'feb': 0, 'aug': 0, 'jan': 0, 'april': 0, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
    {51: {'march': 0, 'may': 1, 'june': 0, 'july': 0, 'feb': 8, 'aug': 0, 'jan': 0, 'april': 2, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
    {48: {'march': 0, 'may': 0, 'june': 4, 'july': 0, 'feb': 0, 'aug': 0, 'jan': 0, 'april': 3, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}},
    {48: {'march': 0, 'may': 0, 'june': 0, 'july': 0, 'feb': 4, 'aug': 0, 'jan': 1, 'april': 0, 'November': 1, 'dec': 0, 'sept': 0, 'oct': 0}}
]

result_dict = {}

for entry in Lst:
    for key, months in entry.items():
        if key not in result_dict:
            result_dict[key] = {month: 0 for month in months}
        for month, value in months.items():
            result_dict[key][month] += value

Result = [{key: value} for key, value in result_dict.items()]

print("Result:")
print(Result)
