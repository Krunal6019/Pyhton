#Decorators

def outer_function():
    message="hello"

    def inner_function():
        print(message)
    return inner_function()
outer_function()



def outer_function():
    message="heyy"

    def inner_function():
        print(message)
    return inner_function

my_func=outer_function()
my_func()

def decorator_function (orignal_function):
    def wrapper_function(*args,**kwargs):
        return orignal_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function run')
display()

@decorator_function
def display_info(name,age):
    print('display_info ran with argument ({},{})'.format(name,age))
display_info('John',23)


# decorator_display=decorator_function(display)
# print(decorator_display()) also yhrows none   
