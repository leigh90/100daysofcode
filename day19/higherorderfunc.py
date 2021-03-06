# add
def add(n1,n2):
    return n1 + n2
# subtract
def subtract(n1,n2):
    return n1 - n2

# multiply
def multiply(n1,n2):
    return n1 * n2

# divide
def divide(n1,n2):
    return n1 // n2

# higher order functions that can call other functions within themselves and execute them
def calculator(n1,n2,func):
    return func(n1,n2)

result = calculator(4,5,multiply)
print(result)