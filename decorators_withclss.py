def decorator_function(original):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed".format(original.__name__))
        return original(*args,**kwargs)
    return wrapper_function

class decorator_class(object):
    def __init__(self,original):#initialize original
        self.original=original
    def __call__(self,*args,**kwargs):#call the wrapper(like)
        print('call method executed')
        return self.original(*args,**kwargs)

@decorator_class
def display():
    print("something great")
#decorated_display=decorator_function(display)
#decorated_display()
@decorator_class
def display2(name,age):
    print("Here the difference can be seen ({},{})".format(name,age))
display2('Piyush',18)
display()
#here we are using class as the decoratorsinstead of functions 