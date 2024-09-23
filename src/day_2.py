


def convert_add(strings:list) -> int:
    return sum([int(i) for i in strings])

test = ['1', '3', '5']

print(convert_add(test))


"""EXTRA CHALLENGE - Duplicate Names"""
import re


def check_duplicates(arr:list):
    if len(arr) < 2:
        return "No Duplicates"
    else:
        dict_arr = {}
        for item in arr:
            dict_arr.setdefault(item, 0)
            pattern = re.compile(item)
            for item in arr:
                if pattern.fullmatch(item):
                    dict_arr[item] += 1
    return [f'{key} has duplicates\n' for key, value in dict_arr.items() if value > 1].__str__()
fruits =['apple', 'orange', 'banana', 'apple', 'orange'] 
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(fruits))