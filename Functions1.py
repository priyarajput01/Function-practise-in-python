#basic method  in functions
#1 add two numbers
def add_two(a, b):
    total = a + b
    return total
result = add_two(5, 4)
print(result)

#2 add two functions
a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
total=add_two(a,b)
print(total)


#3 add two strings
first_name=input("Enter first name")
last_name=input("Enter last name")
print(add_two(first_name,last_name))


#4 add three numbers
def add_three(a, b,c):
    total = a + b + c
    return total 
result = add_three(5, 4,2)
print(result)

#5 user take any input in string then print last element
def last_char(name):
    return name[-1]
print(last_char("priyachauhan"))

#6 odd or even
def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    print(odd_even(2))
    
    
    
#7  even and odd   
def is_even(num):
    if num%2==0:
        return True
    else:
        return False 
print(is_even(a))  


#8 find greater in two numbers
def greater(a,b):
    if a>b:
        return a
    else:
        return b 
num1=int(input("Enter first number"))
num2=int(input("Enter second number")) 
bigger=greater(num1,num2)
print(f"{bigger} is greater")
   

#9 find maximum  in three numbers 
def greatest(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c 
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
bigger = greater(num1,num2,num3) 
print(f"{bigger} is greater") 




    


    
     





