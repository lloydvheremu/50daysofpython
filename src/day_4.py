"""DAY 4: Only Floats"""

def only_floats(a, b) -> int:
    if isinstance(a, float) and isinstance(b, float):
        return 2
    if isinstance(a, float) or isinstance(b, float):
        return 1
    if (isinstance(a, float) or isinstance(b, float)):
        return 0

print(only_floats(12.1, 23))


"""Extra Challenge: index of the Longest Word"""

def word_index(strings:list):
    """
    Since max() and min() return first occurence of string it means they are only equal
    if  all the elements in a list are of the same length, and unequal if elements in a list
    are uneven.
    So we just check if the max() and min() are returning the same string
    """
    longest, shortest = max(*strings, key=len), min(*strings, key=len)
    if longest != shortest:
        # if strings.index(max(*strings)) != strings.index(min(*strings)):
        return longest
    return 0
    
        
words1 = ["Hate", "remorse", "vengeance"]

print(word_index([words1]))

words2 = ["Love", "Hate"]
print(word_index([words2]))
