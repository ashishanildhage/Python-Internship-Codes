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

# #--------------------------- 
# #character is vowel or not(wrong -> in expression, true is not equal to true only for "a" because python evaluates last computed expression, hence only a os vowel not others like e i o u)
# char = "u"
# print("Not Vowel" if char!=("a" or "e" or "i" or "o" or "u") else "Vowel")

# #Vowel or not
# char=(input("Enter Character"))
# alpha="a"<=char<="z" or "A"<=char<="Z"
# vowels="aeiouAEIOU,.$#!"
# if alpha: # dont write char==alpha or char in alpha becuse alpha already has char variable and has checked if true or not before itself
#     print(f"'{char}' is a Vowel" if char in vowels  else "Not Vowel") if char else print("empty")
#     print("vowel" if char=="a" or char=="e" or char=="i" or char=="o" or char=="u" else "Not Vowel")
# else:
#     print("Not an Alphabet")

# #------------------------------    
# #number is divisible by 3 and/or 7 (correct but if dont use elif and use only if then write num%3!=0 and num%7==0 instead of only num%7==0 in elif)
# num=int(input("Enter Number\n"))
# print("divisble by 3 & 7" if num%3==0 and num%7==0 else ( "divisble by 3" if num%3==0 and num%7!=0 else ("divisible by 7" if num%7==0 and num%3!=0 else "not divisible by 3 or 7")))

