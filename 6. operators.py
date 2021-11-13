a=10;b=20
# #Operators
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #Quotient
# print(a%b) #Reminder
# print(a**b) #Power
# print(a//b) #Lowest Integer Quotient

# #Mathematical Operators (Returns only true or false)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b) #tells only true or false not equal value operator
# print(a!=b)
# val=a<b
# print(val)

# #Binary Operators (2 Operands)
# print((a<b) and (a==10))
# print((a<b) or (a==10))
# print(not(a<b)) #a<b is true and not becomes false
# a=0 
# print(a and b) # output 20 (Type conversion - bool(0) and bool(20)), not bool because input operands are int values.x
# print(a or b) # output 10 because 10 is true and since or is used no need to check b hence prints 10
# #print((a+b)and(a/0)) #output is error since infinity
# print((a+b)or(a/0)) #o/p is 30, '''because python evaluates the last computed expression'''
# print("hi" or "hello") #o/p is "hi", because in or first operand "hi" is not empty hence true
# print("" or "hello") #o/p is "hello",since non empty operand

# #Bitwise Operators (not used, since python not good for system bit level programming)
# a=10;b=20
# print(a&b)
# print(a|b)
# print(~a)
# print(a<<b)
# print(a>>b)

# #Shorthand Operators
# a+=2
# a-=2

#precedence of Operators
print(a<b+3)