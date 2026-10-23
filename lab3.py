"""a=int(input("enter principal amount:"))
b=int(input("enter rate:"))
c=int(input("enter time:"))
si=(a*b*c)/100
print(si) """

"""from sys import argv
p=float(argv[1])
q=float(argv[2])
r=float(argv[3])
si=(p*q*r)/100
print(si)
print(argv[0])
print(len(argv))"""

"""s1="python's component"
s2='i study in "GLA"'
print(s1,s2)

str1="Python"
for x in range(len(str1)-1,-1,-1): #(start,end,stop)
    print(str1[x])

for x in range(-len(str1),0): #
    print(str1[x])
for x in range(-1,-len(str1)-1,+1),-1):
    print(str1[x])"""

"""n="puspita priyadarshani das"
print(n[0:7])

a="123456789"
print(int(a[1::2])) #to print even number just change the start value
print(type(n))

#immutable= byte,string,tuple

a="python"
b=4
print(a+b)

a="python"
b=" programming"
print(a+b)

c=('a'*3)+('b'*5)+('c'*6)
print(c)

# 1/sep/2026

str1="python in lab cl4"
print(str1[-1])
print(str1[-len(str1)]) #print first  character using negative indexing
print(str1[5::2])
print(str1[-12:-9:]) #written in this way

str1="123456789"
print(str1[1:5:2])

if 'p' in "python":
    print("yes")
else:
    print("no")

output= print("yes") if 'p' in "Python" else print("no")# print function doesnt return any value so it will return none
print(output)

s1="amit"
s2="anil"
output= s1 if s1<s2 else s2
print(output)
#chronological ordering
 
s1=" amit kumar "
print(len(s1.strip()))
print(len(s1.lstrip().rstrip()))
str1=" amit kumar"
print(str1.find("amit",0,10))
index #find doesnt give error

str1="all that is good is not useful. All that is useful is not good"
print(str1.find("good",14,30))
print("yes")if str1.find("good")==-1 else print ("no")
print("yes") if "good" in str1 else print("no")

dob=input("enter your date of birth in dd/mm/yyyy format:")
day=dob[0:dob.find("/")]
month=dob[dob.find("/")+1:dob.rfind("/")]
dob[dob.rfind("/")+1:]
print("day:",day)
print("month:",month)
print("year:",year)

#22GLA11GLA2024
dob=input("enter your date of birth in ddglammGLAyyyy format:")
sep=input("enter your separator: ")
day=dob[0:dob.find(sep)]
month=dob[dob.find(sep)+1:dob.rfind(sep)]
year=dob[dob.rfind(sep)+1:]
print("day:",day)
print("month:",month)
print("year:",year)"""

""" str1="python is a programming language. python is easy to learn. python is powerful" """

"""print(s1.count("python"))
for i in s1:
    print(i,s1.count(i))
for i in range(len(s1)):
    print(s1[i],s1.count(s1[i]))"""

""" s1.replace("python","java")
print(s1)
print(id(s1))
print(s2)
print(id(s2)) """

#replace function doesnt change the original string it creates a new string and returns it. 
# so we have to assign it to a variable to store the new string

""" s1="ramesh,ansh,aditya,amit,lakshay"
l1=s1.split(",")
l2=l1.split(",")
print(l1)
print(l2)
 """
""" str1=input("enter a string:")
l1=str1.split()
for word in l1:
    print(word, str1.count(word))
 """

""" l1=["ramesh","ansh","aditya","amit","lakshay"]
str="-".join(l1)
print(str)
 """

# blank string is considered as false and non empty string is considered as true in python

"""x=int(input("enter a number:"))
if x<0:
    print("negative")
else:
    print("positive")"""

"""x=int(input("enter a number:"))
y=int(input("enter a number:"))
z=int(input("enter a number:"))
if x>y and x>z:
    print("biggest number is:",x)
elif y>z:
    print("biggest number is:",y)
else:
    print("biggest number is:",z)"""

#answer 1
"""eng=int(input("enter your marks in english:"))
hindi=int(input("enter your marks in hindi:"))
maths=int(input("enter your marks in maths:"))
science=int(input("enter your marks in science:"))
geo=int(input("enter your marks in geography:"))
history=int(input("enter your marks in history"))

sum=(eng+hindi+maths+science+geo+history)
print("sum odf the marks:",sum)
avg=(sum/6)
print("average of the marks:",avg)

a=avg
if a>=90:
    print("grade is A+", "PASSED")
elif a>=80:
    print("grade is A", "PASSED")
elif a>=70:
    print("grade is B+", "PASSED")
elif a>=60:
    print("grade is B", "PASSED")
elif a>=45:
    print("grade is c", "PASSED")
elif a>=33:
    print("grade is D", "PASSED")
else:
    print("fail", "FAILED")"""

""" a=10/3
print("%.2f"%a)
 """
""" item_costs=[10,20,30]
sum=0
for x in item_costs:
    sum=sum + x
print(item_costs)
 """
""" a=input("enter number:")
sum=0
for x in a:
    sum=sum+int(x)
print(sum)
 """
""" a=int(input("enter number:"))
i=0
for x in a:
    if 
    pallindrome check
 
rows=range(1,5)
for x in rows:
    for star in range(5,x-1,-1):
        print("*",end="")
    print()"""

# 10/9/26
""" c=1
for x in range(1,8,2):
    for star in range(x):
        if c%2==0:
            print("*",end="")
        else:
            print("#",end="")
    c+=1
    print() """

""" for x in range(1,6):
    for num in range(x):
        print(x,end="")
    print()
           """      

""" group=[1,2,3,4]
search=int(input("enter the element in the search:"))
for element in group:
    if element==search:
        print("element found")
        break #always at the end of the loop to avoid unnecessary iterations"""

""" cart=[10,20,400,600,800,250]
for item in cart:
    if item>500:
        continue            #continnue statement is used to skip the element which is greater than 500 and continue the loop for the next element
    print("item:", item)  

 """
""" x=10
while x<=12:
    print(x) """
    
""" a=input("enter a string")
print(a[::2])
print(a[1::2])
 """
""" a=input("enter a string:")
b=int(input("enter start index:"))
c=int(input("enter end index:"))
s1=a[b:c:]
s2=s1[c:b:-1]
 """


#pallindrome check
""" a=input("enter a string:")
if a==a[::-1]:
    print("pallindrome")
else:
    print("not pallindrome") """

""" string=input("enter a string:")
s1=string[0:3]
print(s1)
s2=string[-3::]
print(s2)
s3=string[2:8]
print(s3)
s4=string[::-1]
print(s4)
s5=string[::2]
print(s5) """

""" email=input("enter an email")
s1=email[:email.find("@")]
print(s1)
s2=email[email.find("@")+1:]
print(s2) """

#write a python program that takes a long sentence and wraps it to a maximum of 10 characters per line using slicing. each line should not break words.

""" s=input("enter sentence")
start=0
while start <len(s):
    end=s_end=s.find(" ",start)
    while end-start<=9:
       end=s_end
       s_end=s.find(" ")
    print(s[start:end])
    start=end+1 """
#revision

# while- checks condition
#do-while- first work is done then condition is checked

""" total=0
#loop will run atleast once
while true:
 """
#modules and packages

""" x=10
def sum(a,b):
    print("sum of two values",(a+b))
def multiplication(a,b):
    print("multiplication of two values",(a*b)) """

""" import addmultiplication
print(addmultiplication.x)
addmultiplication.sum(1,2)
addmultiplication.multiplication(2,3) """

#python treats a directory as apackage if it c.alled __init__
 
""" def abcd():
    pass
print(abcd())
 """

#LISTS
""" r=range(1,4)
print(r)
print(type(r))
l=list(r)
print(l)
print(type(l))
 """

""" n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4:2])
print(n[3:5]) """

# 17/9/26

""" a=[100,200,300,400]
x=0
while x<len(a):
    print(a[x])
    x=x+1 """

""" n=[1,2,3,5,5,5,6,3]
print(n.count(5))
print(n.count(3))
print(n.count(1)) """

""" n=[10,20,30,40,50]
n.insert(0,76)
print(n) """

""" output:[76, 10, 20, 30, 40, 50] """

""" l1=[10,"anil",23.89,"true"]
l1.append("Dilip")
print(l1)
l1.insert(2,"false")
print(l1)
l1.insert(-23,"rajesh")  #if the index is greater than the max index, then the element will be inserted in last poosition
print(l1)
l1.insert(100,54)         #if the index is smaller than the min index, then the element will be inserted in first position
print(l1)
 """

#if the index is greater than the max index, then the element will be inserted in last poosition
#if the index is smaller than the min index, then the element will be inserted in first position

"""l=[10,20,30,40]
l.insert(-3,222)
print(l)        #important
"""

""" l1=[1,2,3]
l2=["RAHUL","RAJESH","REGINA"]
print("before extend l1 is",l1)
print("before extend l2 is", 12)
l2.extend(l1)
print("after extend l1 is",l1)
print("after extend l2 is",l2)
 """
#l1 will be added in 12

""" n=[1,2,3]
n.remove(2)
print(n) """

# if there is repetition first value will be removed

""" n=[1,2,3,4,5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)
 """
#remove will give value error and pop will give index error
# it returns the popped out element

#reverse()  function

""" n=[1,2,3,4,"two"]
print(n)
n.reverse()
print(n)
 """

""" n=[1,2,3,4,5]
n.sort()
print(n)

s=["suresh", "ramesh", "arjun"]
s.sort()
print(s)

#in sort method , you should only give integer or string otherwise it will give type error

l1=[1,2,3,4,5,6]
l2=l1

l2[1]=34
print(l1)
print(l2) """

#it refers to the same memory. alias

""" l1=[1,2,3,4,5,6]      #imp
l2=l1.copy()

l2[1]=34
print(l1)
print(l2) """

#shallow copy and deep copy
#change will take place in l2 only , it is deep copy

""" x=[10,20,30]
y=x
print(x)
print(y)
print(id(x))   #id means address
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id[y])
 """

""" a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
 """
#type error when list is added with string

""" print([1,2,3]<[2,2,3])
print([1,2,3]<[1,2,3])
print([1,2,3]<=[1,2,4])
print([1,2,3]<[1,2,4])
print([1,2,3]<[0,2,3])
print([1,2,3]==[1,2,3]) """

""" x=["abc","def","ghi"]
y=["abc","def","ghi"]
z=["ABC","DEF","GHI"]
a=["abc","def","ghi","jkl"]
print(x==y)
print(x==z)
print(x==z)

 """

#UPPER CASE IS LOWER THAN LOWER CASE

""" l=[[1,2,3],[4,5,6],"suraj"]
print(1[0][2])
print(1[2][3])
print """

#DATE:18/09/26


#lambda
""" abcd=lambda a :a*2
print(abcd(3))

add=lambda a,b :a+b
print(add(5,6))
 """
#lambda expression is simplest for creating a function


#filter() function

""" items_cost=[999,1100,1500,450,777]
gt_thousand=filter(lambda x: x>1000, items_cost)
x=list(gt_thousand)
print("eligible for discout",x)
 """
#filter will have elements equal to or less than list

""" without_gst_cost=[100,200,300,400]
with_gst_cost=map(lambda x:x+10,without_gst_cost)
x=list(with_gst_cost)
print("without gst items costs", without_gst_cost)
print("wiith gst cost", x) """

#reduce() function returns a value while filter() and map() returns a list

""" from functools import reduce
each_items_costs=[111,222,333,444]
total_cost=reduce(lambda x,y:x+y, each_items_costs)
print(total_cost)
 """

""" from functools import reduce
numbers=[1,2,3,4,5,6]
compare=reduce(lambda x,y: x<y, numbers )
print(compare) """

""" l1=[1,2,3,4,5,6]
l2=list(map(lambda x:x*x,l1))
print(l2)
 
# list comprehension
l3=[z*z for z in l1]
print(l3)
 

l4=list(filter(lambda x:x%2!=0,l1))
print(l4)
l5=[x for x in l1 if x%2==0] """

""" s=range(1,20,3)
for i in s:
    print(i)
m=[x for x in s if x%2==0]
print(m)
 """

#19/09/26
#TUPLES IN PYTHON
#YOU CAN INSERT ANY DATATYPE

""" employee_ids=1,2,3,4,5
print("same type of objects",employee_ids)
print(type(employee_ids))

employee_details=(1,"RGV",100.123)
print("different types of objects", employee_details)


name=("puspita",)
print(name)
print(type(name)) """

#single element in tuple is considered as string , to make it tuple we have to add comma(,) at the end

""" emp_id=()
print(type(emp_id))

emp_id=(11,)
std_id=120,
print(type(emp_id))
print(type(std_id))
 """
""" l=[11,22,33]
t=tuple(l)
print(t)


t=tuple(range(1,10,2))
print(t)

t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
print(t[::2]) """

""" t=(10,20,30,40)
t[1]=70 """
#it gives type error

""" t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)

t1=(10,20,30)
t2=t1*3
print(t2) """

#count() counts occurence

""" t=(10,20,10,10,20)
t1=sorted(t,reverse=True)
print(t1)

t=(40,50,20,10)
t1=sorted(t)
print(t1)
print(min(t))
print(max(t)) """

#TUPLE PACKING
""" a=10
b=20
c=30
d=40
t=a,b,c,d
print(t) """

#TUPLE UNPACKING

""" t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d) """

""" a=12
b=24
print(a,b)
a,b=b,a
print(a,b)
 """

#TUPLE COMPREHENSION

""" t=(x**2 for x in range(1,6))
print(type(t))
print(t)
for x in t:
  print(t) """

#tuple cannot be used as key in dictionary

#DICTIONARIES IN PYTHON

#insertion order is not preserved
""" d={}
d[1]="Ramesh"
d[2]="Suresh"
d[3]="Mahesh"
print(d)

print(d[10])
 """

""" d={1:"ramesh",2:"suresh",3:"Mahesh"}
if 400 in d:
    print(d[400])
else:
    print("key not found") """


""" d={}
n=int(input("enter no. of employees:"))
i=1
while i<=n:
    name=input("enter employee name")
    salary=input("enter employee salary")
    d[name]=salary
    i=i+1
for x in d:
    print("the name is:",x,"and his salary is",d[x])
 """

""" d={1:"ramesh",2:"suresh",3:"Mahesh"}
print("before deleting key from dictionary",d)
del d[1]
print("after deleting key from dictionary",d) """

#clear() to delete the whole dictionary
#list of tuple 
#get method returns none if the index is not present

""" d={1:"GLA MATHURA",2:"GLA NOIDA",3:"GLA LONDON"}
print(d.get(4,"no gla"))

if d.get(4):
    print("hi")
else:
    print("hello") """

""" d={1:"GLA MATHURA",2:"GLA NOIDA",3:"GLA LONDON"}
d.pop(3)
print(d)
d.popitem()
print(d) """

""" squares={a:a*a in range(1,6)}
print(squares) """

""" d={x: x*x for x in range(1,10) if (x*x)%3==0}
print(d)

s={10,20,30,40}
print(type(s)) """

#creating a  set using range funstion
""" s=set(range(5))
print(s) """

""" l1=[1,2,3,3,2,1,2]
d={}
for x in l1:
    if x in d: 
     d[x]+=1
    else:
        d[x]=1
d={k:v for k,v in d.iems() if v>1}
print(d)
l1=list(d.keys()) """
#preseve the sequence

#python doesnt support bitwise method but used in sets

""" t=118613842%9091
print(t)
 """
#FUNCTIONS IN PYTHON
""" def display():
    print("welcome to the function")
display()
display() """

""" def sum(a,b):
    print("sum of two values",(a+b))
sum(20,30)
 """

#function is a block of code which is used to perform a specific task and it can be reused multiple times in the program. it is defined using def keyword.
""" def m1():
    print("this function is returning nothing")
m1()
x=m1()
print(x) """

""" def m1(a,b):
    c=a+b
    d=a-b
    return c,d
x,y=m1(10,5)
print("sum is:",x)
print("subtraction is:",y) """
#tuple unpacking is used to get the values returned by the function. if we want to return multiple values from a function, we can return them as a tuple and then unpack them into separate variables.
""" def m1():
    print("first function information")
def m2():
    print("second function information")
    m1()
m2() """

#FUNTION ARE FIST CLASS OBJECTS
""" def add():
    print("we assigned variable to a function")
    sum=add
sum()

def display():
    print("this is display function")
 """
""" def message(text):
    print("hello"+" " +text)
def printmessage(x):
    x("Puspita") """
printmessage(message)


    