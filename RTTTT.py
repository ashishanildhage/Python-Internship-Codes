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


