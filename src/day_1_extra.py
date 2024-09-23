def longest_value(words:dict) -> str:
    return max(words.values(), key=len)

fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))