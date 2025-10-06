
def square(number):
    return number * number

result = square(5)

print(result)

global_var=10


def global_test():
    print(global_var)
global_test()