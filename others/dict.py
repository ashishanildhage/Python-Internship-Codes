# a=[1,2,3,4]
# b=sorted(a,reverse=True)#sorts the given variable iterable in ascending order (Reverse=true : descending order) and then creates new iterable without changing present one.
# print(b)
# #help(sorted)
# words=["ash","ishh","i","aaaa"]
# c=sorted(words,key=len)#key=len works only on strings not int or float
# print(c)

# #dictionary is a key value mapping
# d={'name':'chandan',# : colon (not = or -), also dont forget to put ,
#    'age':20,
#    'height':5}
# # print(type(d))
# # print(d['name']) # if u give 'nam' which is not given then it says KeyError
# d['phone']='89042' #single = (not double ==)
# # print(d['phone'])

# for k in d:
#     print(k) #to get keys
#     print(k,d[k]) #prints both with space ONE by ONE
#     #above two prints give name,name chandan, age, age 50....

# #Dictionaries are UNORDERED, but list tuples strings are ordered. Hence no guarantee of ordering.
# #dict vs list
# #any immutable type can be a key in dict.
# #dict are very fast to access if u know the key.
# #LIST - inbetween insertion are not constant time, removal not constant time, access only constant time if u know the index 
# #DICT - insertion,removal, access all 3 are constant time.
# print(len(d))

# #dict are passed by reference, after going through function dict modification, their values will be changed when accesed from outside function
# def demo(d):
#     d['name']='ashish'
# demo(d)  #use x=demo(d) only if the function is returning something otherwise not needed.
# print(d['name'])

# #----------------
# #write a program to reverse a dictionary - wrong only one getting printed
# d={'name':'chandan',
#    'age':20,
#    'height':5}
# d2={}

# def reverse(d):
#     for k in d:
#         d2 = {d[k]:k}
#     return d2

# x=reverse(d)
# print(x)

# #correct program
# d={'name':'chandan',
#    'age':20,
#    'height':5}
# def reverse(d):
#     d2={}
#     for k in d:
#         d2[d[k]]=k #very important : new dict[values] = key
#     return d2

# x=reverse(d)
# print(x)

# # -------------
# # generate list of numbers which are squared in new list - wrong
# numbers=[3,6,22,9,60,1]
# i=0
# squared=[]
# while i==len(numbers):
#     squared[i] == [(numbers[i])^2]
#     i+=1
# print(squared)

# #append (add at last in list) function
# a=[1,2]
# a.append(200)
# print(a)

# #correct program
# def square(nos):
#     sq=[]
#     for num in nos:
#         sq.append(num**2)
#         # or sq+=[num**2]
#     return sq #Use list comprehension in python 3 if u have an empty string and want to load data from another string after doing computations

# numbers=[3,5,7]
# n=square(numbers)
# print(n)


# #list comprehension in python - faster than normal for loop
# def square(nos):
#     for num in nos:
#         sq=[num**2 for num in nos]
#     return sq 

# numbers=[3,5,7]
# n=square(numbers)
# print(n)

# #----------
# #create list of n number of elements
# def loadNums(n):
#     return [int(input("Enter no : ")) for i in range(n)]
# nos=loadNums(5)
# print(nos)

# # dictionary comprehension
# d={'name':'chandan',
#    'age':20,
#    'height':5}
# revd={d[k]:k for k in d}
# print(revd)

# #---------------
# #Matrixes using list of list
# #[2 3]
# #[4 5]
# # can be written as:
# mat = [[2,3],[4,5]]
# print(mat[0])
# print(mat[1][0])

#-------------------
# #Take 2*2 square matrix from user and give sum of diagonals - not list of list and also use loop instead of direct add
# def loadNums(n):
#     return [int(input("Enter no : ")) for i in range(n)]

# def add(x):
#     sum = [x[0]+x[2],x[1]+x[3]] 
#     return sum
# x=loadNums(4)
# y=add(x)
# print(y)

# #own code to bet a 2*2 matrix
# def loadNums1(n):
#     return [int(input("Enter no : ")) for i in range(n)]

# def loadNums2(n):
#     return [int(input("Enter no : ")) for i in range(n)]

# def combine(n1,n2):
#     n3=[n1,n2]
#     return n3

# nos3=[]
# nos1=loadNums1(2)
# nos2=loadNums2(2)
# nos3=combine(nos1,nos2)
# print(nos3)

#correct program
n=int(input("Enter size : "))

def loadMat(n):
    mat=[]
    for i in range(n):
        inner=[]
        for j in range(n):
            num=int(input("Enter no : "))
            inner.append(num)
        mat.append(inner)
    return mat

def addDiagonals(mat):
    n=len(mat)
    s1,s2=0,0
    for i in range(n):
        for j in range(n):
            if i==j:
                s1+=mat[i][j]
            if i+j==n-1: #it should be if not elif because in [1,1,1],[1,1,1],[1,1,1] the output will be 3 and 2 not 3 and 3
                s2+=mat[i][j]
    return s1,s2        

m=loadMat(n)
print(m)         
s1,s2 = addDiagonals(m)          
print(s1,s2)    


