# Simple Function

def greet():
    print("Welcome to Python Functions")

    greet()

# Function with Parameter

def greet_user(name):
    print("Hello", name)

greet_user("Dnyanesh")

# Function with return value

def add(a, b):
    return a + b
result = add(10,5)
print("Sum :", result)

# Default Parameter
def country(name="India"):
    print("Country:", name)

country()
country("USA")
