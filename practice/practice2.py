#functions in python
import sys

print(sys.path)
def hello_func():
    #pass
    print("hello function")


    hello_func()

def hey_func(greeting):
    return '{} function.'.format(greeting)

def hy_func(greeting,name='You'):
    return '{} ,{} '.format(greeting,name)


#print(hey_func('hi'))
print(hy_func('hi','krunal'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

    
student_info('Math','Art',name='John',age='22')