#1 Palindrone function
def is_palindrone(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
print(is_palindrone("naman")) 
print(is_palindrone("priya"))  


#2 print function
def user_info(first_name,last_name,age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")
user_info('Harshit','vasisth',24)  




#3 Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum([8, 2, 3, 0, 7]))

#4 write a program functionto print all the multiply numbers in a list
def multiply(numbers):
    total = 0
    for a in numbers:
        total *= a
    return total
print(multiply([8,2,3,0,7]))   

#5 Factorial number
def factorial(n):
    if n == 0:
        return 0
    else:
        return n* factorial(n-1)
n = int(input("Input a number to compute the factorial:"))
print(factorial(n)) 


#6 Write a Python function to check whether a number falls within a given range.
def test_range(n):
    if n in range(3, 9):  # Checks if n is within the range 3 to 8 (inclusive)
        print("%s is in the range" % str(n))  # Prints if n is in range
    else:
        print("The number is outside the range")  # Corrected the message

# Call the function with a number as an argument
test_range(5) 


#7 Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):  # Use a valid name for the parameter (e.g., lst)
    x = []  # Create an empty list to store unique elements
    for a in lst:  # Iterate over each element in the input list
        if a not in x:  # If the element is not already in x, add it
            x.append(a)
    return x  # Return the list of unique elements

# Call the function with a list of numbers
print(unique_list([1, 2, 2, 3, 3, 3, 3, 4, 5]))


#8 Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]
def is_even_num(1):
    enum = []
    for i in 1:
        if n % 2 == 0:
            enum.append(n)
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])) 
             