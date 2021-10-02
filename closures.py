#closures allow us to take advantage of first class functions and returns an inner 
#function that remembers and executes(has access to) variables local to scope in
#whuch they were created

def outer(msg):
    def inner():
        print(msg)
    return inner#not executing
   #return inner() executing

display_hi=outer('hi')
display_hi()
#it helps us to understand the concept of decorators