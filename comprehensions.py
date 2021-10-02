#in this exercise we will learn about list comprehension
nums=[1,2,3,4,5,6,7,8,9,10]
list1=[]
for i in nums:
   list1.append(i)
print(list1)
# now list comprehensions
list1=[i for i in nums]
print(list1)
#some more complex example
list1=[i*i for i in nums]
print(list1)

#now using map+lambda(anonymous)
list1=map(lambda n: n*n*n,nums)
print(list1)
# one more example
list2=[]
for i in nums:
   if i%2==0:
      list2.append(i)
print()
#another version
list2=[i  for i in nums if i%2==0]
print(list2)

list3= []
for i in 'abcd':
   for j in range(4):
      list3.append((i,j))
print(list3,end="")
# list comprehension of this above
list3=[(i,j) for i in 'abcd'for j in range(4)]
print(list3)
#now dictionary comprehensions
name=['piyush','arun','vicky','mohit']
surname=['bagani','fs','sfsaf','afasf']
mydict={}
for name,surname in zip(name,surname):
   mydict[name]=surname
print(mydict)
#now comprehensions
mydict={name: surname for name,surname in zip(name,surname) if name!='piyush'}
print(mydict)
#set comprehensions
num=[1,1,1,1,1,2,2,2,2,3,5,4,3,3,5]
myset=set()
for i in num:
   myset.add(i)
print(myset)
#comprehensions
myset={i for i in num}
print(myset)
#generator expressions
"""def gens(nums):
   for i in nums:
      return i*i
my=gens(nums)"""
#com
my=(i*i for i in nums)
for i in my:
   print(i)