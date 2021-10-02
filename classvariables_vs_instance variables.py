class Employee:
    def __init__(self,fname,lname,pay):
        self.fname=fname#These are Instance Variables
        self.lname=name
        self.pay=pay
        self.email=fname + ' ' + lname + ' ' +'@gmail.com'

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

emp1=Employee("piyush",'Bagani',100000000)
p=emp1.fullname()
print(p)
print(Employee.fullname(emp1))#here we have called fullname method with Employee

#for class variables

class Employee:
    empno=0
    raise_amount = 1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname#These are Instance Variables
        self.lname=lname
        self.pay=pay
        self.email=fname + '' + lname + '' +'@gmail.com'
        Employee.empno+=1

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)
    def amount(self):
        self.pay = int(self.pay * self.raise_amount) #or  self.pay = int(self.pay * Employee.raise_amount)
        #here self.raise_amount can be wriiten as Employee.raise_amount but keeping self
        #will selp because constant can be overidden easily and we can change raise amount
        #for a particular employee if we want which is not possible with class Employee like
emp1=Employee("piyush",'Bagani',100000000)
p=emp1.fullname()
print(p)
print(Employee.fullname(emp1))#here we have called fullname method with Employee
print(emp1.pay)
emp1.amount()
print(emp1.pay)



#we can see namespace
print(emp1.__dict__)
Employee.raise_amount=1.05
emp1.raise_amount=1.03
print(emp1.__dict__)
print(Employee.__dict__)

#another use is when we
# cant use self (instance) and we have to use the Employee(classname) because 
# no. of employees cant be combined with simgle instance
print(Employee.empno)
emp2=Employee("piyush",'Bagani',100000000)
print(Employee.empno)