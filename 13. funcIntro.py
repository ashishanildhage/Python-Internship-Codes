#only thing that u need is what is input and output and name of function and a few rules to use, u dont need to know what is there in the function.
def add(a,b):         #function defination
    return round(a+b) #if there is no return then the function has no output
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
