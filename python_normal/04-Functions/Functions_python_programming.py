print("Variable length Arguments..")
print("Positional Arguments...")

def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1,2,3,4,5,6,7,8,9)

def print_numbers_upd(*args,**kwargs):
    for number in args:
        print(f"Positional Arguments {number}")
    for key,value in kwargs.items():
        print(f"{key}-->{value}")

print_numbers_upd(1,2,3,4,5,6,7,8,9,name="Dipanjan",age=38)


print("Program: Checking the strongness of a password")

def password_checker(pwd):
    """This function checks the strongness of a password"""
    if len(pwd)<8:
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    if not any(char.islower() for char in pwd):
        return False
    if not any(char.isupper() for char in pwd):
        return False
    if not any(char in '!@#$%^&*()_+=' for char in pwd):
        return False
    
    return True

pwd = "Jun17@2908"
status = password_checker(pwd)
print(f"The {pwd} is {status}")
print("Working")

print("*" * 100)
print("The lambda function details...")

addition = lambda x,y,z: x+y+z
print(addition(5,10,15))

print("The usage of map function")

numbers = [1,2,3,4,5,6,7]

print(list(map(lambda num: num**2,numbers)))

print("Map function with multiple iterable")

iter1 = [1,2,3]
iter2 = [4,5,6]

result_set = map(lambda x,y: x+y,iter1,iter2)

print(list(result_set))

print("The filter function usage")

input = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda x:x%2==0,input))

print(result)