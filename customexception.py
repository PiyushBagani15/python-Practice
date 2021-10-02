# A python program to create user-defined exception 
# class MyError is derived from super class Exception 
class MyError(Exception): 

	# Constructor or Initializer 
	def __init__(self, value): 
		self.value = value 

	# __str__ is to print() the value 
	def __str__(self): 
		return(repr(self.value)) 

try: 
	raise(MyError(3*9))

# Value of Exception is stored in error 
except MyError as error: 
	print('A New Exception occured: ',error.value) 
