# #------------------------
# a=[1,2,"hello","hi",2.5]
# # lists are mutable, they can be changed. but strings arent mutable.
# a[0]=300
# print(a)
# nos=[1,2] + [2,3] #lists can be concatenated. 
# #you can store anything in the lists. but can store only one datatype in array. this is the difference
# print(nos,max(nos))

# words = ["abc","c", "dd"]#lexicographical order
# print(max(words))#it checks for the highest character of any length
# # help(max)
# print(max(words,key=len))#if 2 elements have same length then it will show first one as max


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
#list(dictionary) gives output : key only that is LHS as list - Very Important
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
