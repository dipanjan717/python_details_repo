# This is the first comment of python programming

print("This is the first comment of python programming")

print("Multiple statements in single line")

x = 5 ; y = 10 ; z = x + y
print("z:", z)

# Type inference

type(z)

user_input = input("Enter Your Name : ")
print(f"You have entered {user_input}")

print(100 * "=")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")

print("**Question 10:** Write a Python program to check if a variable is of a specific data type.")

var = 1.7

if isinstance(var,float):
    print(f"{var} is a float")
else:
    print(f"{var} is not a float")

print("Write a Python program to sort a list of numbers in ascending order.")

numbers = [ int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
print(f"Sorted List : {numbers}")