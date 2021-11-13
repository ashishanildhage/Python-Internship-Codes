# a=10;b=20
# #Trueexpr1 if boolexpr else Falseexpr2
# msg = "Lesser"  if a<b  else "Greater"
# print(msg)

# a=(input("Enter first number") or 0) 
# print("") if a else print(f"Assuming {a}.\n")
# b=(input("Enter Second Number") or 0) 
# print("") if b else print(f"Assuming {b}.\n")
# a,b=int(a),int(b)
# print(a+b if a==b else a-b)

# #-------------------
# #Which is greater among 3 numbers?
# a=input("Enter first number ") or 0
# b=input("Enter Second Number ") or 0
# c=input("Enter Third Number ") or 0
# a,b,c=int(a),int(b),int(c)
# max_of_2 = b if b>a else a
# max_of_3 = c if c>max_of_2 else max_of_2
# print(f"{max_of_3} is greater")

# #----------------------
# #even or odd program (Full program is wrong - python takes float when u use divide ie, quotient)
# #q=5/2
# #>>> type(q)
# #<class 'float'>
# #>>> q=10/2
# #>>> type(q)
# #<class 'float'>
# #case-1
# num=10
# quo=num/2
# print("Even" if str(type(quo))=="<class 'int'>" else "Odd") #This is wrong code.

# #case-2
# num=11
# print("Odd" if (num-2*(num//2)) else "Even")

# #case-3
# num=11
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")