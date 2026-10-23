#FUNCTIONS
"""def first():
    print("this is outer function")
    def second():
        print("this is inner function")
    second() #local
#calling outer function
first()

def first():
    def second():
        print("this function is return type to outer function")
    return second
x=first()
x()

def createfunctions():
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    return add,sub
x,y=createfunctions()
print(x(10,5))
print(y(10,5))

#TYPES OF ARGUMENTS IN FUNNCTION
def sum(a,b):
    c=a+b      #a and b are formal arguments
    print(c)
#call the function
x=10
y=15
sum(x,y)    #x and y are actual arguments

#positional arguments
def info(name,roll):
    print("name:",name)
    print("roll:",roll)
info("Puspita",29) #positional argument
info(name="Puspita",roll=29) #keyword argument

#default arguments
def cart(item,price=20):
    print(item,price)
cart(item="ball") #if we dont give any value in price, it will take 20 as default

def total_cost(x,*y):
    print(type(x))
    print(type(y))
    sum=0
    for i in y:
        sum+=1
    print(x+sum)
total_cost(100,200)
total_cost(110,226,311)
total_cost(11,)

print(type(x))
print(type(y))

def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
print_kwargs(id=1,name="jack",qualification="MBA")"""

#local variable
"""def m():
    a=11
    print(a)
def n():
    print(a)  #local vaiable will give error
m()
n()
#global variable
a=11
b=12
def m():
    print(a)
    print(b)
def n():
    print(a)
    print(b)
m()
n()"""

""" def m():
    a=11
    print(a)
m()

def m():
    a=11
    print(a)
def n():
    print(a)
m()
n()
 """
#name error

""" def add(x,y,z):
    return x+y+z
def add(x,y,z,w):
    return x+y+z+w """
#it will give error because python does not support function overloading. The last defined function will be called.

""" a=1
def m1():
    a=2
    print(a)
def m2():
    print(a)
m1()
m2()

a=1
def m1():
    global a
    a=2
    print(a)
def m2():
    print(a)
m1()
m2() """
#here a is modified using the global variable

""" a=1
def m1():
    a=2
    print(a)
    print(globals()["a"])
m1() """
#RECURSIVE FUNCTION

""" 1.termination condition """
""" def d1(x):
    if x==11:
        return
    else:
        print(x)
        d1(x+1)
d1(1)
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
print(fact(5)) """

s=input("enter string").lower().split()
Total_words=len(s)
print("Total_words:",Total_words)
a=
