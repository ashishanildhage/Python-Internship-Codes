# name=input("Enter the name : ")
# times=int(input("Enter the times : "))
# i=1
# columns=2
# while i<=times:
#     j=0
#     while j<columns:
#         print(f"{i}. {name} ",end="")
#         i+=1
#         j+=1
#         if i==times-1: 
#             break
#     print("")  
    
     
# sum=0    
# num=eval(input("Enter number:"))
# while type(num) is not str:
#     try:
#         num=eval(input("Enter number:"))
#         sum+=num
#     except:
#         print(sum)
#         break
    
# str=input("Enter number")
# for i in str:
#     if i=="0":
#         str=str[:i]+"9"+str[i+1:]
# print(str)

# s=input("Enter the string : ")
# choice=input("L or R? -> ")
# def rotate(string,choice):
#     if choice=="L":
#         string<<1
#         return string
#     elif choice=="R":
#         string>>1
#         return string
#     else:
#         return "invalid choice"
    
# out=rotate(s,choice)
# print(out)

# def addthem(no1):
#     def take(no2):
#         nonlocal no1
#         no1+=1
#         return no1+no2
#     return take
        
# out=addthem(20).take(10)
# print(out)

# a=["ashish","happy","imagine","share","grow","give","imaginf"]
# def add(a):
#     return a[:len(a)-1]
    
# out=list(map(add,a))
# print(out)

# a=["ashish","happy","imagine","share","grow","give","imaginf"]
# out=list(map(lambda a:a[:len(a)-1],a))
# print(out)
# out=list(filter(lambda a:a[len(a)-1]=="e",a))
# print(out)
