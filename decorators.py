#decortors is function  that adds functionality to other function(makes it cool)
#by taking that as an arguement and returns without altering the original code 
# of function
def decorator_function(original):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed".format(original.__name__))
        return original(*args,**kwargs)
    return wrapper_function


#@decorated_function cannot be written over two functions untill (*args,**kwargs) is not passed to wrapper 
@decorator_function
def display():
    print("something great")
#decorated_display=decorator_function(display)
#decorated_display()


@decorator_function
def display2(name,age):
    print("Here the difference can be seen ({},{})".format(name,age))
display2('Piyush',18)
display()