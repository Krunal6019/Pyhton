def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args,**kwargs):
            print(prefix,'Executed Before',original_function.__name__)
            result=original_function(*args,**kwargs)
            print(prefix,'Executed After',original_function.__name__,'\n')
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator('TEST:')
def dispaly_info(name,age):
    print('dispaly_info ran with arguments ({},{})'.format(name,age))

dispaly_info('Trump',76)