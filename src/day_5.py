"""
Day 5: My Discount
"""

def my_discount() -> float:
    price = float(input("Enter price: "))
    discount = float(input("Enter % Discount as decimal: "))

    return price - price * discount

# print(my_discount())

"""
EXTRA CHALLENGE: TUPLE OF STUDENT SEX
"""

def students_sexes(students:list) -> list:
    males = 0
    females = 0
    for student in students:
        if student.lower() == 'male':
            males += 1
        if student.lower() == 'female':
            females += 1
    
    return [('Male', males), ('female', females)]

students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']


print(students_sexes(students))