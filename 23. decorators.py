# #BASICS OF PYTHON DECORATORS
# #add 10 to 20
# def makeAdder(a):
#     def add(b): #add is a variable in makeAdder which is referring to the makeAdder function
#         nonlocal a#not local to the add function, not global , but global to the makeAdder function
#         a+=1
#         return a+b
#     return add #function closure

# f=makeAdder(10)
# v=f(20)
# print(v)
# print(f(30)) #output is 42 not 41 because previous value will get stored in itself in "a" variable whenever function gets called
# # print(makeAdder(50))
# # print(v(30))

# v=makeAdder(10)(20) #function carrying
# print(v)

# '''
# v(10)
# v
# makeAdder(10).add(10) #>>>'function' object has no attribute 'add'
# makeAdder
# f(10)
# f
# add(10)
# add
# '''
# #if u modify a variable within a function then local scope of varible will get off

