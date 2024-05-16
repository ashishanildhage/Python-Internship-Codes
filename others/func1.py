#only thing that u need is what is input and output and name of function and a few rules to use, u dont need to know what is there in the function.
def add(a,b):         #function defination
    return round(a+b,ndigits=1) #if there is no return then the function has no output
r=add(3.2,4.79)       #function call. # the def function code is run only when it is called.
print(r)              #print function defination called output

'''this type function which returns something is called FRUITFUL FUNCTION
if function doesnt return anything then it returns none
first understand what function does what is input and whether it gives output and then do work
you cant call a function before defining it because python interpreter reads line by line. not like other languauges where acceptable
dont use print function in own defined function instead use return, because that will become command line output whichis not accepted by industry
so always return the output and then use it for furthur tasks for GUI  or webpage without printing. only return.
so always print seperately after funciton is called and processed
DUCK TYPING means if +1 is operation then any datatype on which +1 operation is valid input. it will work.
if programmer is idiotic and novice, then python will have less security, but java will take care of security since it accepts only particular elements like only int no float etc. thus java compiler is strict and checks.but python doesnt
'''


#Local Variable concept
n=10         #even if n is made global variable, output will still remain 11 and 10
def inc():   #function context n and file context variable n are not the same, both are different.
    global n
    print(n) #if interpreter cant find n value in local scope of function then only it will find n in parent scope
    n+=1     #n is available only for function
    return n #only returns value of 11 not the function variable n 
val=inc()    #after function call, when output is returned the functions variables will get deleted until called next time
print(val)   #output is 11
print(n)     #output is 10

#error - UnboundLocalError: local variable 'n' referenced before assignment
#if no argument is given in inc() in both call and defination

#fucntional programming more valuable than OOP, one function performs only one task. it shouldnt do more than one work.

#------------------------
#write a program to rotate the string -  Wrong code : Left and right shift operators are bitwise not character wise
s=input("Enter the string : ")
choice = input("Enter L or R to rotate : ")
def rotate(string,choice):
    if choice == "L":
        string<<1
        return string
    elif choice == "R":
        string>>1
        return string
out = rotate(s,choice)
print(out)

#this is how u write a code which is testable - neat and clean
def rotateLeftOnce(s):
    return s[-1]+s[:-1]
#always have 1 line gap between 2 functions - design standard rules for coding
def rotateRightOnce(s):
    return s[1:]+s[0]

def rotate(s,direction,times):
    for i in range(0,times):
        if direction.upper() == "L":
            s=rotateLeftOnce(s)
        elif direction.upper() == "R":
            s=rotateRightOnce(s)
    return s #dont forget to add return s in function code. 

s=input("Enter the string : ")
choice = input("Enter L or R to rotate : ")
times = int(input("Enter the number of times : "))
print(rotate(s,choice,times))

'''programmer and software developer are different roles. programmer - how ever u do, work must be done with. developer - code must be neat and clean and should be fast and testable
requirements specifications - functional and non functional requirements
non- func req - speed performance code size improving
functions in python are first class objects - one can assign a function to a variable
'''

#you can pass a function as argument to another function
def work(f):
    f()

def foo():
    print("Foofoo")

f=foo #it wont call the function #if the function has return then use f=foo() else if nothing is returned then use f=foo
f()
work(f)

#function inside function
def work(f):
    f()

def bar(): #writing a function/machine which builds another function/machine. machine manufacturing machine
    def foo():
        print("Foofoo bar")
    return foo
f=bar()
f()
work(f)


#BASICS OF PYTHON DECORATORS
#add 10 to 20
def makeAdder(a):
    def add(b): #add is a variable in makeAdder which is referring to the makeAdder function
        nonlocal a#not local to the add function, not global , but global to the makeAdder function
        a+=1
        return a+b
    return add #function closure

f=makeAdder(10)
v=f(20)
print(v)
print(f(30)) #output is 42 not 41 because previous value will get stored in itself in "a" variable whenever function gets called
# print(makeAdder(50))
# print(v(30))

v=makeAdder(10)(20) #function carrying
print(v)

'''
#what are these??????
v(10)
v
makeAdder(10).add(10) #>>>'function' object has no attribute 'add'
makeAdder
f(10)
f
add(10)
add
'''
#if u modify a variable within a function then local scope of varible will get off


#------------------------
a=[1,2,"hello","hi",2.5]
type(a) # lists are mutable, they can be changed. but strings arent mutable.
a[0]=300
print(a)
nos=[1,2] + [2,3] #lists can be concatenated. 
#you can store anything in the lists. but can store only one datatype in array. this is the difference
print(nos,max(nos))

words = ["abc","c", "dd"]#lexicographical order
print(max(words))#it checks for the highest character of any length
# help(max)
print(max(words,key=len))#if 2 elements have same length then it will show first one as max


#inline functions
#if function has one argument, one line and one return statement then u can convert it into lambda function
#map function - it will run one function on every literable and it gives output appending to a new list
nos=[3,4,5]
def sq(x):
    return x**2

l=list(map(sq,nos))#first function and then list/string to be iterated one after another
print(l)
#map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.
#allows you to process and transform all the items in an iterable without using an explicit for loop

l=list(map(lambda x:x**2,nos))
print(l)

#filter function - iterates through string/list and gives values which are true into new string/list
nos=[3,4,5]
l=list(filter(lambda e:e%2==0,nos)) # output will be 4 in a list
print(l)
#list(dictionary) gives output : key only that is LHS as list
#filter - allows you to process an iterable and extract those items that satisfy a given condition


# -------------------------------
# using functools reduce function
#if u write this code then u r hired - calculate sum of list
nos=[3,4,5]
import functools 
s=functools.reduce(lambda a,b:a+b,nos) #reduces entire iterable into a single value like sum of the list.
#it takes 2 numbers, and the result will be passed as first argument for next iterable operation aka accuulator to give output at last
print(s)

#hence map is for connecting function expression, filter for condition True creating and functools.reduce reduces iterable to one value but requires 2 values together as a,b

# GENERATORS
# u can write function which returns a value and then the functions local variables dont get destroyed, they get retained.
# this is called as generator. design pattern subject
# append function eats lot of time for lots of data in big list,hence slow. To remove this use generator
# producer and consumer result function. one function output(producer) acts as input for antoher function(consumer). 
# producer if creates too much and consumer consumes very little then it will be problem. Eg: food at home waste.
# called as on the fly production
# maruti has car ready before getting order, but lambourgini produces car after they get order so wastage doesnt happe. same applies for coding

nos=[3,4,5]
def sq(x):
    for elem in nos:
        yield elem**2

#return returns only 3**2 and breaks the loop, but yield is like printing return into the object, all 3 are returned and doesnt break until the funciton ends
f=sq(nos)
print(f) # gives output <generator object sq at 0x00000263F0519E40>. It generator is ready to give output
print(next(f)) #only one value is consumed so only one production. one call,one number generate until nothing is left
print(next(f))
print(next(f))
# #print(next(f))#error - StopIteration
# #if u want to consume everything just loop
f=sq(nos)# dont forget to write this to refresh the generator from past next function values
for e in f:
    print(e)

#ur not using generator or the right data structure if u get timeout error runtime for large data.

#----------------------
#Generator Comprehension
nos=[3,4,5]
f=(e**2 for e in nos)#generator comprehension without using function. yield e**2 gives invalid syntax error
print(next(f))
for e in f:
    print(e)
#even if print next f and then for loop also output will be 9 and then 16 25 without error.

#default arguments in function
def add(a=10,b=20): #def add(a,b=20) then a is a compulsory argument. add(a=10,b) IS NOT ALLOWED. since the arg u give while calling will be first arg in function
    return a+b
v=add(2,3)
print(v)#5
print(add(4))# 4 will be "a" and "b" will be default 20. op is 24
print(add())#30


#----------------------------
#variable length arguments(VARL)
def add(*numbers):
    return numbers+numbers#DOUBLES THE LIST only, it doesnt do like lambda a,b:a+b

a=add(1,2,3,4,5)#it is printing tuples
print(a)

nos=[3,4,5]
import functools
def add(*numbers):
    return functools.reduce(lambda a,b:a+b,numbers)

print(add(nos))




