"""DAY 3 Challenge : Register Check"""

def register_check(students:dict) -> int:
    number_of_students = 0
    if len(students) > 0:
        for key, value in students.items():
            if value == 'yes':
                number_of_students +=1
    return number_of_students

names = {'Michael':'yes','John': 'no','Peter':'yes', 'Mary': 'yes'}
print(register_check(names))    
        
"""Extra Challenge -Lowercase Names"""

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
def lowercaseNames(names:list):
    names = [name for name in names if name.islower()]
    return set(names)

print(lowercaseNames(names))

