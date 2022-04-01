#string formatting differnt methods
person ={'name': 'Piyush', 'age' : 21}
sent ="My Name is {} and my age is {}".format(person['name'],person['age'])
sente="My Name is {0} and my age is {1}".format(person['name'],person['age'])
#another way
#sente="My Name is {0[name]} and my age is {1[age]}".format(person,person)
#if we pass {0[name] and 0[age] and .format (person)} then also it will work
l=['Piyush',19]
sente="My Name is {0[0]} and my age is {0[1]}".format(l)
sente="My Name is {name} and my age is {age}".format(name='Piyush',age=19)#more readable with dictionary
sente="My Name is {name} and my age is {age}".format(**person)#most convenient method

print(sent)
print(sente)

#html tags
tag = 'hi'
text ='this is headline'
senten='<{0}>{1}</{0}>'.format(tag,text)
print(senten)

#working with  objects
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age


p1=Person('Piyush',19)
sentence="My Name is {0.name} and my age is {0.age}".format(p1)
print(sentence)

#formatting numbers

for i in range(1,11):
    sentence1="The value  is  {:01}".format(i)
    print(sentence1)

#formatting decimals
pi=3.14287232345
sentence2="the value of pi is : {:.3f}".format(pi)
print(sentence2)

sen="1 MB is equal to {:,.2f}".format(1000**2)#comma separated 
print(sen)

#formatting date time
import datetime as dt
mydate = dt.datetime(2020,9,24,12,30,45)
#print(mydate)
sentence3="the date is :{:%B %d, %Y}".format(mydate)
#this formatting can be seen on documentations
print(sentence3)

sentence4= '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(mydate)
print(sentence4)