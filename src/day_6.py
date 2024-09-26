"""
Day 6: User Name Generator
"""

def user_name() -> str:
    email = input("Enter Email")
    name = email.split('@')[0]
    return name


# print(user_name())

"""
Extra Challenge: Zero Both Ends"""

def zeroed(arr:list) -> list:
    if len(arr) > 1:
        arr[0] = 0
        arr[-1] = 0
        return arr

    return arr

inputt = [2, 5, 7, 8,]
print(zeroed(inputt))