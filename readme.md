# 50 Days of Python: A Challenge a Day
## Day 1: Division and Square-root
### Write a function called divide_or_square that takes one argument (a number), and returns the square root of the number if it is divisible by 5, returns its remainder if it is not divisible by 5. 
> For example, if you pass 10 as an argument, then your function 
should return 3.16 as the square root
#### Extra Challenge: Longest Value
>Write a function called longest_value that takes a dictionary as an argument and returns the first longest value of the dictionary. For example, the following dictionary should return – apple as the longest value. fruits = {'fruit': 'apple', 'color': 'green'}

## Day 2: Strings to integers
### Write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list. 
> For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9
#### Extra Challenge: Duplicate Names
> Write a function called check_duplicates that takes a list of strings as an argument. The function should check if the list has any duplicates. If there are duplicates, the function should return the duplicates. If there are no duplicates, the function should return "No duplicates". For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates". fruits =['apple', 'orange', 'banana', 'apple'] names = ['Yoda', 'Moses', 'Joshua', 'Mark']

## Day 3 
### Write a function called register_check that checks how many students are in school. The function takes a dictionary as a parameter.  If the student is in school, the dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’. Your function should return the number of students in school. Use the dictionary below. 
> Your function should return 3.register ={'Michael':'yes','John': 'no','Peter':'yes', 'Mary': 'yes'}
#### Extra Challenge: Lowercase Names
> names = ["kerry", "dickson", "John", "Mary", carol", "Rose", "adam"] You are given a list of names above. This list is made up of names of lowercase and uppercase letters. Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters. Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return: ('kerry', 'dickson', 'carol', 'adam')

## Day 4
### Write a function called only_floats, which takes two parameters a and b, and returns 2 if both arguments are floats, returns 1 if only one argument is a float, and returns 0 if neither argument is a float,
> If you pass (12.1, 23) as an argument your function should return a 1
#### Extra Challenge: Index of the Longest Word
> Write a function called word_index that takes one argument, a list of strings and returns the index of the longest word in the list. If there is no longest word (if all the strings are of the same length), the function should return zero (0).For example, the list 
below should return 2. words1 = ["Hate", "remorse", "vengeance"] And this list below, should return zero (0) words2 = ["Love", "Hate"]

## Day 5: My Discount
### Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. Once the user inputs the price and discount, it calculates the price after the discount. The function should return the price after the discount. 
> For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.

#### Extra Challenge: Tuple of Student Sex
> You work for a school and your boss wants to know how many female and male students are enrolled in the school. The school has saved the students in a list. Your task is to write a code that will count how many males and females are in the list. Here is a list below:students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female'] Your code should return a list of tuples. The list above should return: [(‘Male’,7), (‘female’,6)]

## Day 6: User Name Generator
### Write a function called user_name that generates a username from the user’s email. The code should ask the user to input an email and the code should return everything before the @ sign as their user name.
> For example, if someone enters ben@gmail.com, the code should return ben as their user name.
#### Extra Challenge: Zero Both Ends
> Write a function called zeroed code that takes a list of numbers as an argument. The code should zero (0) the first and the last number in the list. For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0]