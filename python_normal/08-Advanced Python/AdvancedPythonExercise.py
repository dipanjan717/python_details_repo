list1 = [1,2,3,4,5,6]
iter1 = iter(list1)
print(type(iter1))



try:
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
except Exception as ex:
    print(ex)


print("Generator Understanding...")

def large_file_read(file_path):
    with open(file_path,"r") as file:
        for line in file:
            yield line

file_path = 'large_file.txt'
for line in large_file_read(file_path):
    print(line.strip())

print("Decorator Functions ...")

print("Function copy...")

def welcome():
    return "Welcome to Avanced Python Course"

wel = welcome
print(wel())

del welcome

print(wel())

print("Closoure function...")

def outer_welcome(func):
    msg = "Welcome to the class"
    def inner_function():
        print("Welcome to advanced python course.")
        func()
        print("Please focus on all the activites of the class.")
    return inner_function()

# outer_welcome(print)

print("Decorator Function...")

@outer_welcome
def course_introduction():
    print("Introduction to Avanced Python course")



# One more example

def my_decorator(func):
    msg = "Welcome to the class"
    def wrapper():
        print("Something is happening before the function ...")
        func()
        print("Something is happening after the function ...")
    return wrapper

# outer_welcome(print)

print("Decorator Function...")

@my_decorator
def course_introduction():
    print("Introduction to Avanced Python course")

course_introduction()